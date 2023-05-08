#!/bin/sh

# Set the path to your news.py script (adjust the path accordingly)
SCRIPT_PATH="./search-gpt.py"

# Auto-detect the path for the Python interpreter
PYTHON_PATH=$(command -v python3 || command -v python)

# Check if Python is installed
if [ -z "$PYTHON_PATH" ]; then
    echo "Error: Python is not installed."
    exit 1
fi

# Run the Python script
$PYTHON_PATH $SCRIPT_PATH "$@"
