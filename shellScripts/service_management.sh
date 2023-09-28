#!/bin/bash

# Define the maximum number of days of inactivity to consider a service as unnecessary
MAX_INACTIVITY_DAYS=30

# Get a list of all services and their statuses
SERVICE_LIST=$(systemctl list-units --type=service --all --no-pager --plain | awk '{print $1,$3}')

# Loop through the services and check their inactivity
for service_status in $SERVICE_LIST; do
  service=$(echo "$service_status" | cut -d' ' -f1)
  status=$(echo "$service_status" | cut -d' ' -f2)

  # Check if the service is active
  if [ "$status" == "active" ]; then
    # Get the last activation time of the service
    last_activation=$(systemctl show -p ActiveEnterTimestamp "$service" | cut -d= -f2)

    # Calculate the number of days since the service was last activated
    days_since_activation=$(( ( $(date +%s) - $(date -d "$last_activation" +%s) ) / 86400 ))

    # Check if the service has been inactive for more than MAX_INACTIVITY_DAYS
    if [ $days_since_activation -ge $MAX_INACTIVITY_DAYS ]; then
      echo "Disabling $service (Inactive for $days_since_activation days)..."
      systemctl disable "$service"
      systemctl stop "$service"
    fi
  fi
done

# Reload systemd to apply changes
systemctl daemon-reload

echo "Service management complete."

