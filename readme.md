##Read me

#plotting and manual selection of size or area data for fractal or lognormal datasets

```python
%matplotlib qt

import fractal_finder as ff
```


```python
path = "/path/to/data"
file_path = "Sample_clasts.csv"
sample_name ="Clasts1"
```


```python
slope, intercept, r_value, xdata, ydata = ff.fit_fractal_slopes(file_path, path, sample_name)
```

    Please click upper and lower limits: 
    ('clicked: ', [(0.040635815694876627, 68.702772243672825), (0.7325538838902671, 7.2002636460899856)])



```python
r_squared = ff.fit_lognormal(file_path, path, sample_name)
```

    Please click upper and lower limits: 
    ('clicked: ', [(0.0052143269702835653, 126.10133557974061), (2.5403276214454706, 2.853977921358299)])

