#!/bin/bash

# USB Port Protection Script

# Define the path to the udev rules file
UDEV_RULES_FILE="/etc/udev/rules.d/99-usb-port-protection.rules"

# Check if the script is run as root
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root. Please use sudo."
    exit 1
fi

# Check if the udev rules file already exists
if [ -e "$UDEV_RULES_FILE" ]; then
    echo "USB port protection rules already exist. Aborting."
    exit 1
fi

# Create udev rules file to disable USB ports
cat <<EOL > "$UDEV_RULES_FILE"
# Disable USB ports
SUBSYSTEMS=="usb", ENV{authorized_default}="0"
EOL

# Reload udev rules
udevadm control --reload-rules

# Inform the user
echo "USB port protection is now active. USB ports are disabled."

# To enable USB ports again, you can remove the udev rules file and reload rules.
# Uncomment the following lines to re-enable USB ports.
# rm "$UDEV_RULES_FILE"
# udevadm control --reload-rules

exit 0
