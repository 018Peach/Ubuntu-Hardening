#!/bin/bash

# Ask the user if they want to perform actions on a file
read -p "Do you want to perform actions on a file in the current directory? (y/n): " choice

if [ "$choice" = "y" ]; then
    # List files in the current directory
    echo "Files in the current directory:"
    ls

    # Prompt the user for the filename
    read -p "Enter the filename: " filename

    # Check if the file exists
    if [ -e "$filename" ]; then
        # Ask the user what action they want to perform
        read -p "Do you want to (e)ncrypt or (c)hange permissions on the file? (e/c): " action

        if [ "$action" = "e" ]; then
            # Encrypt the file using GPG
            gpg -c "$filename"

            if [ $? -eq 0 ]; then
                echo "File '$filename' encrypted successfully."
            else
                echo "Encryption failed for '$filename'."
            fi
        elif [ "$action" = "c" ]; then
            # Ask the user for the new file permissions
            read -p "Enter the new file permissions (e.g., 600, 644, etc.): " permissions

            # Change file permissions using chmod
            chmod "$permissions" "$filename"

            if [ $? -eq 0 ]; then
                echo "File permissions changed for '$filename' to $permissions."
            else
                echo "Failed to change file permissions for '$filename'."
            fi
        else
            echo "Invalid action. Please enter 'e' for encrypt or 'c' for change permissions."
        fi
    else
        echo "File '$filename' does not exist."
    fi
elif [ "$choice" = "n" ]; then
    echo "No actions will be performed on files."
else
    echo "Invalid choice. Please enter 'y' for yes or 'n' for no."
fi

exit 0
