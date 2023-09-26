#!/bin/bash

# List of services you want to enable (replace these with the services you need).
# For example, if you want to enable "sshd" and "nginx," list them here.
services_to_enable=("sshd" "nginx")

# List of services you want to disable (replace these with the services you want to disable).
# For example, if you want to disable "telnet" and "ftp," list them here.
services_to_disable=("telnet" "ftp")

# Loop through the services to enable and start them
for service in "${services_to_enable[@]}"; do
    systemctl enable "$service"
    systemctl start "$service"
    echo "Enabled and started $service"
done

# Loop through the services to disable and stop them
for service in "${services_to_disable[@]}"; do
    systemctl stop "$service"
    systemctl disable "$service"
    echo "Stopped and disabled $service"
done

# Reload systemd to apply changes
systemctl daemon-reload

echo "Service management complete"
