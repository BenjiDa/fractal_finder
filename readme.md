<p align="center">
  <img width="584" alt="logo" src="https://user-images.githubusercontent.com/18178879/55429311-04e69900-5540-11e9-8775-9b5924d6f5bc.png">
</p>

# Read me

## Plotting and manual selection of size or area data for fractal or lognormal datasets. This interactive module is designed to work with jupyter notebook.

### Import
```python
%matplotlib qt

import fractal_finder as ff
```

### Add path and file name information
```python
path = "/path/to/data/" #Path to your data
filename = "Sample_clasts.csv" #File in .csv format
sample_name ="Clasts1" #Name of sample, used to save bestfits
```

### Run fractal finder (interactive plot)
```python
slope, intercept, r_value, xdata, ydata = ff.fit_fractal_slopes(filename, path, sample_name)
```

<img width="621" alt="frctl" src="https://user-images.githubusercontent.com/18178879/55427159-41fc5c80-553b-11e9-9a0f-7eb71a324451.png">

### Run lognormal fit window (interactive plot)
```python
r_squared = ff.fit_lognormal(filename, path, sample_name)
```

<img width="593" alt="lgnrm" src="https://user-images.githubusercontent.com/18178879/55427169-458fe380-553b-11e9-933a-c5e0b6395581.png">

