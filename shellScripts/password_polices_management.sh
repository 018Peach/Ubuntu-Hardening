#!/bin/bash

# Install PAM-related tools if not already installed
sudo apt-get install libpam-pwquality libpam-cracklib

# Configure password quality requirements in /etc/security/pwquality.conf
cat <<EOL | sudo tee /etc/security/pwquality.conf
minlen = 12
minclass = 3
maxrepeat = 2
maxsequence = 4
reject_username
enforce_for_root
EOL

# Configure password policies in /etc/security/pwquality.conf
cat <<EOL | sudo tee /etc/security/pwquality.conf
password requisite pam_pwquality.so retry=3
password requisite pam_pwquality.so minlen=12 minclass=3 maxrepeat=2 maxsequence=4
EOL

# Set password expiration policy in /etc/security/pwquality.conf
sudo sed -i 's/PASS_MAX_DAYS.*/PASS_MAX_DAYS   90/' /etc/login.defs
sudo sed -i 's/PASS_MIN_DAYS.*/PASS_MIN_DAYS   7/' /etc/login.defs
sudo sed -i 's/PASS_WARN_AGE.*/PASS_WARN_AGE   7/' /etc/login.defs

# Force users to change their password on next login
sudo chage -d 0 <username>

# Print a message indicating the password policies have been configured
echo "Password policies have been configured."

# Restart the PAM service to apply changes
sudo systemctl restart systemd-logind
