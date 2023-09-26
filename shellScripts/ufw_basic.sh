#!/bin/bash

# Install UFW if not already installed
sudo apt install ufw -y

# Configure UFW rules
sudo ufw default deny incoming  # Deny incoming traffic by default
sudo ufw default allow outgoing  # Allow outgoing traffic by default
sudo ufw allow ssh  # Allow SSH access (customize as needed)
sudo ufw enable  # Enable the firewall
