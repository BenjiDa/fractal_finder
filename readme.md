# Read me

## Plotting and manual selection of size or area data for fractal or lognormal datasets. This interactive module is designed to work with jupyter notebook.

### Import
```python
%matplotlib qt

import fractal_finder as ff
```

### Add path and file name information
```python
path = "/path/to/data/"
file_path = "Sample_clasts.csv"
sample_name ="Clasts1"
```

### Run fractal finder (interactive plot)
```python
slope, intercept, r_value, xdata, ydata = ff.fit_fractal_slopes(file_path, path, sample_name)
```

### Run lognormal fit window (interactive plot)
```python
r_squared = ff.fit_lognormal(file_path, path, sample_name)
```

