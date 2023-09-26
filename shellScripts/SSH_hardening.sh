#!/bin/bash

# Edit SSH configuration file to enforce security settings

#effectively disables the ability for the root user to log in via SSH.
sudo sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config

#disables password-based authentication, meaning users will need to use SSH keys for authentication.
sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

#restarts the SSH service to apply the changes made to the SSH configuration.
sudo systemctl restart ssh
