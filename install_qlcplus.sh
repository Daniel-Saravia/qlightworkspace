#!/bin/bash
# Daniel Saravia
# STG-452: Capstone Project II
# February 2, 2025
# Check if QLC+ is installed
if command -v qlcplus &> /dev/null; then
    # Retrieve the installed version of QLC+
    INSTALLED_VERSION=$(qlcplus --version 2>&1 | grep -oP '(\d+\.\d+\.\d+)')
    echo "QLC+ is already installed. Version: $INSTALLED_VERSION"

    # Define the latest available version
    LATEST_VERSION="4.13.1"
    
    # Compare installed version with the latest version
    if [ "$INSTALLED_VERSION" == "$LATEST_VERSION" ]; then
        echo "You already have the latest version of QLC+ installed."
        exit 0
    else
        echo "A newer version of QLC+ is available. Updating to version $LATEST_VERSION..."
    fi
else
    echo "QLC+ is not installed. Installing the latest version..."
fi

# Update the system packages to ensure latest dependencies are installed
sudo apt update && sudo apt upgrade -y

# Install necessary dependencies for QLC+
sudo apt install -y build-essential cmake qt5-qmake qtbase5-dev qtchooser qtbase5-dev-tools libqt5svg5-dev libeigen3-dev libhidapi-dev libftdi-dev wget

# Define the URL to download the latest QLC+ version
LATEST_DEB_URL="https://www.qlcplus.org/downloads/4.13.1/qlcplus_4.13.1_amd64.deb"

# Download the QLC+ package from the official website
wget $LATEST_DEB_URL -O qlcplus_4.13.1_amd64.deb

# Install the downloaded .deb package using dpkg
sudo dpkg -i qlcplus_4.13.1_amd64.deb

# Fix any missing dependencies if required
sudo apt --fix-broken install -y

# Remove the downloaded .deb file to free up space
rm qlcplus_4.13.1_amd64.deb

# Confirm successful installation and display installed version
echo "QLC+ has been successfully installed/updated to version:"
qlcplus --version
