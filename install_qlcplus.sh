#!/bin/bash

# Check if QLC+ is installed
if command -v qlcplus &> /dev/null; then
    INSTALLED_VERSION=$(qlcplus --version 2>&1 | grep -oP '(\d+\.\d+\.\d+)')
    echo "QLC+ is already installed. Version: $INSTALLED_VERSION"

    # Check if the installed version is the latest
    LATEST_VERSION="4.13.1"
    if [ "$INSTALLED_VERSION" == "$LATEST_VERSION" ]; then
        echo "You already have the latest version of QLC+ installed."
        exit 0
    else
        echo "A newer version of QLC+ is available. Updating to version $LATEST_VERSION..."
    fi
else
    echo "QLC+ is not installed. Installing the latest version..."
fi

# Update the system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y build-essential cmake qt5-qmake qtbase5-dev qtchooser qtbase5-dev-tools libqt5svg5-dev libeigen3-dev libhidapi-dev libftdi-dev wget

# Download the latest QLC+ version
LATEST_DEB_URL="https://www.qlcplus.org/downloads/4.13.1/qlcplus_4.13.1_amd64.deb"
wget $LATEST_DEB_URL -O qlcplus_4.13.1_amd64.deb

# Install the downloaded .deb package
sudo dpkg -i qlcplus_4.13.1_amd64.deb

# Fix dependencies if necessary
sudo apt --fix-broken install -y

# Clean up the downloaded .deb file
rm qlcplus_4.13.1_amd64.deb

# Confirm installation
echo "QLC+ has been successfully installed/updated to version:"
qlcplus --version