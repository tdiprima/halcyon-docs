#!/bin/bash

# build_sphinx.sh
# Bash script to build Sphinx documentation

# Set the SOURCE and BUILD directories
SOURCE_DIR=.
BUILD_DIR="build"

# Check if Sphinx is installed
if ! command -v sphinx-build &> /dev/null
then
    echo "Sphinx is not installed. Please install Sphinx to continue."
    exit 1
fi

# Build the documentation
echo "Building Sphinx documentation..."
sphinx-build -b html "$SOURCE_DIR" "$BUILD_DIR"

# Check if the build was successful
if [ $? -eq 0 ]; then
    echo "Documentation built successfully."
else
    echo "Failed to build documentation."
    exit 1
fi

