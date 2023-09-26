#!/bin/bash

# Define administrative and regular user names
admin_user="adminuser"
regular_user="regularuser"

# Define a list of default and unused user accounts to be removed or locked
default_users=("guest" "user1" "user2")
unused_users=("unuseduser1" "unuseduser2")

# Create administrative user account
echo "Creating administrative user account: $admin_user"
useradd -m -s /bin/bash $admin_user
passwd $admin_user
usermod -aG sudo $admin_user

# Create regular user account
echo "Creating regular user account: $regular_user"
useradd -m -s /bin/bash $regular_user
passwd $regular_user

# Remove or lock default user accounts
for user in "${default_users[@]}"
do
    if id "$user" &>/dev/null; then
        echo "Removing default user account: $user"
        userdel -r $user
    else
        echo "User account not found: $user"
    fi
done

# Lock unused user accounts
for user in "${unused_users[@]}"
do
    if id "$user" &>/dev/null; then
        echo "Locking unused user account: $user"
        passwd -l $user
    else
        echo "User account not found: $user"
    fi
done

# Clean up temporary files
echo "Cleaning up temporary files"
rm -f /tmp/temporary_file

echo "User and group management completed."
