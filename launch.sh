#!/bin/bash

# Compile w/ Cython
python setup.py build_ext --inplace

# Launch script
python main.py
