# algosDS
Algorithms and Data Structures

## Getting Started

To get a working environment there are two possible options.

1. Create a conda environment with the listed pre-requisites
2. Create a conda environment from the .yml file

### Dependencies
```
python 3.8.5
pytest 6.1.1
```
### Installation
To get started make sure you either have the listed pre-requisites or set up the anaconda environment from the .yml file.
```
conda env create -f environment.yml
```
Make sure you activate the environment.
```
conda activate algo_ds
```
Verify that it was properly installed.
```
conda env list
```
And finaly actovate the environment.
```
conda activate algo_ds
```

## Tests
For running all tests write:




a
```
pytest tests
```
For running some specific tests write (e.g. two_number_sum):
```
pytest tests/test_two_number_sum.py
```
For omitting a particular test, go to the file containing the test and add the following decorator to the test function:
```
@pytest.mark.skip(reason="Should not be run because...")
```

