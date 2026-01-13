# ===============================
# ANACONDA & CONDA BASIC COMMANDS
# ===============================

# Check conda version
conda --version

# Update conda
conda update conda

# List all installed packages
conda list

# Search for a package
conda search numpy

# Install a package
conda install numpy

# Update a package
conda update numpy

# Remove a package
conda remove numpy


# ===============================
# CONDA ENVIRONMENT COMMANDS
# ===============================

# Create a new environment with Python version
conda create --name myenv python=3.10

# Activate the environment
conda activate myenv

# Deactivate the environment
conda deactivate

# List all environments
conda env list

# Remove an environment
conda remove --name myenv --all

# Export environment to a file
conda env export > environment.yml

# Create environment from file
conda env create -f environment.yml


# ===============================
# JUPYTER LAB COMMANDS
# ===============================

# Install Jupyter Lab
conda install -c conda-forge jupyterlab

# Launch Jupyter Lab
jupyter lab

# Launch Jupyter Notebook (optional)
jupyter notebook

# Check Jupyter version
jupyter --version

# List running Jupyter servers
jupyter server list

# Stop Jupyter server (Ctrl + C in terminal)


# ===============================
# USE ENVIRONMENT IN JUPYTER
# ===============================

# Install ipykernel
conda install ipykernel

# Add conda environment to Jupyter
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
