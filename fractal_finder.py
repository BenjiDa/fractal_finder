import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

path = "your/path/"
file ="data.csv"


data = pd.read_csv(path+file)
df = pd.DataFrame(data)
sort_area = df.sort_values('Area',ascending=False)#sort pandas datafram decending


sort_area['int_index'] = range(len(df))

#define x, y data
xdata = sort_area['Area']
ydata = sort_area['int_index']



def fit_fractal_slopes(xdata, ydata):
    
    #Function that calculates best fit to a fractal portion of a size distribution curve. 
    #Data must be sorted by size before, function plots data and allows user to interactively select
    #fractal portion of the size distribution curve. Returns d-value and displays on graph.
    
    def powerlaw(x, amp, index): #fractal geometry equation
        return amp * (x**index)

    def fitfunc(p, x, y): #linear representation of fractal equation
        return (y - (p[0] + p[1] * x))
    
    xtext = min(xdata)#position for d-value label at end of plot
    
    ax = plt.loglog(sort_area['Area'],sort_area['int_index'],'k.')#plot all data
    plt.ylabel('Clast count')
    plt.xlabel('Clast size (cm^2)')
    plt.gca().set_aspect('equal')#set equal aspect ratio for plot.
    
    print("Please click upper and lower limits: ")#interactively select log-linear portion of curve
    x = plt.ginput(2, show_clicks=True)
    print("clicked: ", x)
    y_fit_range = np.append(int(x[0][1]), int(x[1][1]))

    xdata = xdata[min(y_fit_range):max(y_fit_range)]#crop data to log-linear portion of curve
    ydata = ydata[min(y_fit_range):max(y_fit_range)]
    logx = np.log(xdata)#convert data for linear fitting
    logy = np.log(ydata)
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(logx, logy)

    
    plt.loglog(xdata,ydata,'bo',mew='0.3') #plot best fit interval
    plt.loglog(xdata,powerlaw(xdata,np.exp(intercept),slope), 'r-')#plot best fit
    plt.text(xtext,1,'d-value: %s, r-squared: %s' % (abs(round(slope,2)), round(r_value**2,3)), style='italic',size=12,ha='left',va='bottom')

    return slope, intercept, r_value
