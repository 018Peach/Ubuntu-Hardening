#!/bin/bash

# Check if ufw is installed, and install it if not
if ! command -v ufw &> /dev/null; then
  sudo apt install ufw -y
fi

# Function to apply UFW rules from a configuration file
apply_ufw_rules() {
  local config_file="$1"
  # Check if the configuration file exists
  if [ -f "$config_file" ]; then
    echo "Applying UFW rules from $config_file..."
    sudo ufw --force reset  # Reset existing rules
    sudo ufw --force enable
    sudo ufw --force reload
    sudo ufw --force --import="$config_file"  # Import rules from the config file
  else
    echo "Configuration file $config_file not found. Exiting."
    exit 1
  fi
}

# Prompt the user for their choice
echo "Select an option:"
echo "1. Prevent Tor (block Tor traffic)"
echo "2. Deny incoming traffic (default)"
echo "3. Allow incoming traffic (open firewall)"
echo "4. Load custom configuration from a file"

read -p "Enter the number of your choice: " choice

# Configure UFW rules based on the user's choice
case $choice in
  1)
    # Block Tor traffic
    echo "Blocking Tor traffic..."
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    sudo ufw allow ssh
    TOR_EXIT_NODES_URL="https://check.torproject.org/torbulkexitlist"
    curl -sS $TOR_EXIT_NODES_URL | while read -r ip; do
      sudo ufw deny from $ip
    done
    ;;
  2)
    # Deny incoming traffic
    echo "Denying incoming traffic..."
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    sudo ufw allow ssh
    ;;
  3)
    # Allow incoming traffic
    echo "Allowing incoming traffic..."
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    sudo ufw allow ssh
    ;;
  4)
    # Load custom configuration from a file
    read -p "Enter the path to the UFW configuration file: " config_file
    apply_ufw_rules "$config_file"
    ;;
  *)
    echo "Invalid choice. Exiting."
    exit 1
    ;;
esac

echo "UFW configured as per your choice."
