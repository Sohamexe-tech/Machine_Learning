# Environment Setup Notes

## Step 1: Install Anaconda
Download from: https://www.anaconda.com/products/distribution
Choose Python 3.9+ version for your OS.

## Step 2: Create the Conda Environment
```bash
conda create -n ml_ds_env python=3.9 numpy pandas
```

## Step 3: Activate the Environment
```bash
conda activate ml_ds_env
```

## Step 4: Install Additional Packages
```bash
conda install scikit-learn matplotlib seaborn
conda install notebook jupyterlab
```

## Step 5: Verify Installation
```bash
conda --version
python --version
```

## Step 6: Verify Libraries (inside Python interpreter)
```bash
python
>>> import numpy as np
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> from sklearn.model_selection import train_test_split
>>> exit()
```

## Step 7: Launch JupyterLab
```bash
jupyter lab
```

## Step 8: Export Environment (for sharing/reproducibility)
```bash
conda env export > environment.yml
```

## Step 9: Recreate Environment from File
```bash
conda env create -f environment.yml
```

## Common Issues
- 'conda not recognized': Restart terminal or use Anaconda Prompt on Windows
- 'ModuleNotFoundError': Make sure your environment is activated before installing
- Version conflicts: Create a fresh environment and install packages one by one