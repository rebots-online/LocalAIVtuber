#!/bin/bash

# Set environment variables
export PYTHONNOUSERSITE=1
export PYTHONPATH=
export PYTHONHOME=
export CUDA_PATH=/usr/local/cuda
export CUDA_HOME=/usr/local/cuda

# Activate virtual environment
source venv/bin/activate

# Install GPU-specific dependencies
pip install --upgrade torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

echo "Switched to GPU successfully."
