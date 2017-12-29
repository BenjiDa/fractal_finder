import pandas as pd


path = "/your/data/"
file ="data.csv"


data = pd.read_csv(path+file)
df = pd.DataFrame(data)
sort_area = df.sort_values('Area',ascending=False)#sort pandas datafram decending


sort_area['int_index'] = range(len(df))

#define x, y data
xdata = sort_area['Area']
ydata = sort_area['int_index']


fit_fractal_slopes(xdata, ydata)

