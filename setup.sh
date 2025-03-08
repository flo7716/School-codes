#!/bin/bash

# Create a new conda environment named jpn_florian with Python 3.8
conda create -n jpn_florian python=3.8 -y

# Activate the new environment
source activate jpn_florian

# Install required dependencies
conda install -y pandas scikit-learn matplotlib seaborn jupyter

# Install any additional dependencies using pip if needed
pip install -r requirements.txt

echo "Environment setup complete. To activate the environment, use: conda activate jpn_florian"