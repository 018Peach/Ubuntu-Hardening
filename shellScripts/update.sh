#!/bin/bash

# Update the package lists and upgrade installed packages
sudo apt update
sudo apt upgrade -y

# Remove unused packages (orphans) and their configuration files
sudo apt autoremove --purge -y

# Clean up package cache to free up disk space
sudo apt clean

echo "All updates and cleanup completed."
