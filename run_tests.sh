#!/bin/bash

# -----------------------------
# Script to run Dash test suite
# -----------------------------

# Name of your virtual environment folder
VENV_DIR="venv"

# Path to your test file
TEST_FILE="test_app.py"

# Exit on any error
set -e

# Activate virtual environment
if [ -f "$VENV_DIR/Scripts/activate" ]; then
    # Windows Git Bash / WSL
    source "$VENV_DIR/Scripts/activate"
elif [ -f "$VENV_DIR/bin/activate" ]; then
    # Linux / macOS
    source "$VENV_DIR/bin/activate"
else
    echo "ERROR: Could not find virtual environment in $VENV_DIR"
    exit 1
fi

# Run pytest
echo "Running test suite..."
pytest -v "$TEST_FILE"
TEST_EXIT_CODE=$?

# Deactivate virtual environment
deactivate

# Return exit code
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "All tests passed ✅"
    exit 0
else
    echo "Some tests failed ❌"
    exit 1
fi
