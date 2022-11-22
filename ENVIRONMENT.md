# Environment Setup

This document describes special features in this `environment.yaml` as well as usage.

## Install

To install this environment, please install a conda-compliant package manager. Then,

```shell
conda env update -f environment.yaml
```

The resulting environment is called `paleoPandas`

```shell
conda activate paleoPandas
```

## Pandas Nightly Installation

Since we are working with newer pandas features, we usually choose to install a pandas nightly version.
The nightly packages are hosted at [pypi.anaconda](https://anaconda.org/scipy-wheels-nightly/pandas/files).

The environment.yaml files has some special directives that are used for pip to point it to the proper
channels to install from. In this case, we add the repository using the `--extra-index-url` flag. [Example Usage](https://github.com/conda/conda/blob/main/tests/conda_env/support/advanced-pip/environment.yml)

```yaml
dependencies:
  ...
  - pip:
    - --extra-index-url https://pypi.anaconda.org/scipy-wheels-nightly/simple
    - pandas==2.0.0.dev0+664.g86f182829d
```

## Running Notebooks

We will launch within this environment, so the default kernel in Jupyter will contain all the packages. Currently,
some of the example notebooks are broken. To run jupyterlab, do:

```shell
jupyter lab --port=<port_address>
```

The default port address is 8888 if not specifying the port.
