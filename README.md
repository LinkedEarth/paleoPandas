# paleoPandas
Exploring working with Pandas time axis for paleoclimate data.

Example Notebook through MyBinder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/khider/paleoPandas/HEAD)

## Setup

In order to run these example locally, you'll first need to clone the repo:

```
git clone 
```

Navigate into the repo directory:

```
cd paleoPandas
```

Now you'll build a conda environment to ensure that all the required packages
are installed. 

```
conda env create -f environment.yml
```

Then activate the environment:

```
conda activate paleopandas
```

You are ready to launch JupyterLab and get started running the examples! 

```
jupyter lab
```

## Data sources

| Filename | Source |
| -------- | ------ |
| tortugas2011.xls | https://www.ncei.noaa.gov/pub/data/paleo/coral/atlantic/tortugas2011.xls


## Developer setup

For those working on development of this repo, please install the pre-commit 
hook to ensure that notebook contents are cleared before committing to the repo. 
This helps us keep the repo size down so its quick to download.

```
pre-commit install
```
