#!/bin/bash

# Example: Restrict permissions for sensitive file
sudo chmod 600 /path/to/sensitive-file
#600 allows only root user to read and write 


sudo chown root:root /path/to/sensitive-file
#Changes ownership to root user, only root user has access to read and write