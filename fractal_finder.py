import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit
import json


def data_loader(file, path):
    

    data = pd.read_csv(path+file)
    df = pd.DataFrame(data)
    sort_area = df.sort_values('Area',ascending=False)#sort pandas datafram decending


    sort_area['int_index'] = range(len(df))

    xdata = sort_area['Area']
    ydata = sort_area['int_index']
    
    return xdata, ydata

def pick_fit_section(xdata, ydata):
    
    ##Function that lets you pick portion of the curve to fit a function to, 
    #returns x and y data over the user-selected range.
    

    print("Please click upper and lower limits: ")#interactively select log-linear portion of curve
    x = plt.ginput(2, show_clicks=True)
    print("clicked: ", x)
    y_fit_range = np.append(int(x[0][1]), int(x[1][1]))

    
    xdata = xdata[min(y_fit_range):max(y_fit_range)]#crop data to log-linear portion of curve
    ydata = ydata[min(y_fit_range):max(y_fit_range)]
    
    return xdata, ydata

def powerlaw(x, amp, index): #fractal geometry equation
        return amp * np.power(x,index)
    

    
def fit_fractal_slopes(file, path, sample_name):
    
    #Function that calculates best fit to a fractal portion of a size distribution curve. 
    #Data must be sorted by size before, function plots data and allows user to interactively select
    #fractal portion of the size distribution curve. Returns d-value and displays on graph.
    
    xdata, ydata = data_loader(file, path)

    def fitfunc(p, x, y): #linear representation of fractal equation
        return (y - (p[0] + p[1] * x))
    
    xtext = min(xdata)#position for d-value label at end of plot
    
    fig = plt.figure()
    ax = plt.loglog(xdata,ydata,'k.')#plot all data
    plt.ylabel('Clast count')
    plt.xlabel('Clast size (cm^2)')
    plt.gca().set_aspect('equal')#set equal aspect ratio for plot.
    
    xdata, ydata = pick_fit_section(xdata, ydata)
    
    logx = np.log(xdata)#convert data for linear fitting
    logy = np.log(ydata)
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(logx, logy)
    
    store_data_fractal(sample_name, slope, intercept, r_value, path)

    #plt.loglog(xdata,ydata,'bo',mew='0.3') #plot best fit interval
    
    plt.loglog(xdata,powerlaw(xdata,np.exp(intercept),slope), 'r-')#plot best fit
    plt.text(xtext,1,'d-value: %s, r-squared: %s' % (abs(round(slope,2)), round(r_value**2,3)), style='italic',size=12,ha='left',va='bottom')
    #plt.savefig('/Users/bmelosh/Dropbox/Serpentinite_flow/analyses/fractal/%s_fractal.pdf' % sample_name)
    
    return slope, intercept, r_value, xdata, ydata


def fit_lognormal(file, path, sample_name):
    
    # Function that calculates a log-normal fit over a manually selected range of data.

    xdata, ydata = data_loader(file, path)
    
    def func(x, mu, sigma, N):
        return (N*(np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))/ (x * sigma * np.sqrt(2 * np.pi))))
    
    fig = plt.figure()
    plt.loglog(xdata, ydata, 'k.', label='data')
    plt.gca().set_aspect('equal')#set equal aspect ratio for plot.
    xtext = min(xdata)
    xdata, ydata = pick_fit_section(xdata,ydata)
    
    popt, pcov = curve_fit(func, xdata, ydata)
    
    #Calculate r-squared
    residuals = ydata - func(xdata, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((ydata-np.mean(ydata))**2)
    r_squared = 1 - (ss_res / ss_tot)
    
    store_data_curve(sample_name, popt, r_squared, path)
    
    plt.loglog(xdata, func(xdata, *popt),'r')#,label='fit: a=%5.3f, b=%5.3f' % tuple(popt))
    
    plt.text(xtext, 1, 'R squared: %s' % round(r_squared,3), style='italic',size=12,ha='left',va='bottom')
    
    return r_squared

def store_data_fractal(sample_name, slope, intercept, r_value, path):
    d = {}
    d["name"] = sample_name
    d["slope"] = slope
    d["intercept"] = intercept
    d["r_squared"] = r_value**2
    #d["xdata"] = xdata.values.tolist()
    
    with open(path + '%s_bf_fractal.txt' % sample_name, 'w') as fp:
        json.dump(d, fp)

    
def store_data_curve(sample_name, popt, r_squared, path):
    popt_list = popt.tolist()
    d = {}
    d["name"] = sample_name
    d["popt"] = popt_list
    d["r_squared"] = r_squared
    #d["xdata"] = xdata.values.tolist()
    
    with open(path + '%s_bf_curve.txt' % sample_name, 'w') as fp:
        json.dump(d, fp)

