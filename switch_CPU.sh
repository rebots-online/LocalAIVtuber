#!/bin/bash

# Set environment variables
export PYTHONNOUSERSITE=1
export PYTHONPATH=
export PYTHONHOME=
export CUDA_PATH=
export CUDA_HOME=

# Activate virtual environment
source venv/bin/activate

# Install CPU-specific dependencies
pip install --upgrade torch==2.2.2 torchaudio==2.2.2

echo "Switched to CPU successfully."
