#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install llama-cpp-python

# Install nltk data
pip install nltk
python -m nltk.downloader -d /usr/local/share/nltk_data all

# Start the program
python main.py
