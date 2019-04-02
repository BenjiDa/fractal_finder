# Read me <img width="584" alt="runner_w" src="https://user-images.githubusercontent.com/18178879/55427180-49236a80-553b-11e9-867e-3031f46b25bf.png">


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

<img width="621" alt="frctl" src="https://user-images.githubusercontent.com/18178879/55427159-41fc5c80-553b-11e9-9a0f-7eb71a324451.png">

### Run lognormal fit window (interactive plot)
```python
r_squared = ff.fit_lognormal(file_path, path, sample_name)
```

<img width="593" alt="lgnrm" src="https://user-images.githubusercontent.com/18178879/55427169-458fe380-553b-11e9-933a-c5e0b6395581.png">
