#!/bin/bash

# Check if the script is running with root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root."
  exit 1
fi

# Install auditd if it's not already installed (you can skip this step if auditd is already installed)
if ! command -v auditd &>/dev/null; then
  echo "Installing auditd..."
  apt-get update
  apt-get install auditd -y  # Use 'yum' for Red Hat-based systems
fi

# Enable auditd service
systemctl enable auditd
systemctl start auditd

# Create a custom audit rule file (e.g., /etc/audit/rules.d/custom-audit.rules)
audit_rule_file="/etc/audit/rules.d/custom-audit.rules"

# Define custom audit rules
cat <<EOL >"$audit_rule_file"
# Monitor file system changes
-w /etc/passwd -p wa -k passwd_changes

# Monitor user login and authentication events
-w /var/log/auth.log -p wa -k login_events

# Add more custom rules here
EOL

# Reload auditd rules
auditctl -R "$audit_rule_file"

# Set auditd configuration parameters (customize as needed)
auditctl -e 2  # Set to 2 for enabled, 0 for disabled
auditctl -b 8192  # Set buffer size (adjust as needed)
auditctl -f 1  # Enable filtering

# Restart auditd to apply changes
systemctl restart auditd

# Display status information
echo "Audit logging has been enabled and configured."
echo "You can review audit logs in /var/log/audit/audit.log."
