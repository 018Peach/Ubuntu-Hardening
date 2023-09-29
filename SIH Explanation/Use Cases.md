
# Use Cases

Here are all the use cases of the application

## 1. Patch Management

Patch management is the process of keeping your system's software and operating system up to date by applying security updates and patches. It's essential to protect your system from known vulnerabilities and exploits. The `apt` package manager is a package management tool commonly used in Debian-based Linux distributions (such as Ubuntu) to ensure that all installed software and packages are current by regularly checking for updates and applying them.

Example script:
```bash
#!/bin/bash
# Update the package list
sudo apt update
# Upgrade all installed packages to their latest versions
sudo apt upgrade -y
# Apply security updates
sudo apt dist-upgrade -y
# Remove obsolete packages
sudo apt autoremove -y
```

Output:
```
>>
 Hit:1 http://security.ubuntu.com/ubuntu focal-security InRelease
 Get:2 http://us.archive.ubuntu.com/ubuntu focal InRelease [265 kB]
 Get:3 http://us.archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]
 ...
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
   package1 package2 package3
 ...
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be REMOVED:
   orphaned-package1 orphaned-package2
 ...
Reading package lists... Done
Building dependency tree       
Reading state information... Done
 0 upgraded, 0 newly installed, 0 to remove and 2 not upgraded.

All updates and cleanup completed.

```

This script first updates the list of available packages, then upgrades all installed packages to their latest versions, including security updates. It also removes any obsolete packages that are no longer needed.
## 2. Firewall

A firewall is a security system that controls and monitors incoming and outgoing network traffic to and from your system. Proper firewall configuration is crucial to restrict unauthorized access to your system. `ufw` (Uncomplicated Firewall) is a user-friendly firewall management tool for Linux. Configuring ufw allows you to define rules that specify which services and ports are allowed or denied for network communication.

Example Script:
```bash
#!/bin/bash
# Deny all incoming and outgoing traffic by default
sudo ufw default deny incoming
sudo ufw default deny outgoing
# Allow SSH (replace 22 with your SSH port if necessary)
sudo ufw allow 22/tcp
# Allow HTTP and HTTPS
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
# Enable the firewall
sudo ufw enable
```

Output:
```
>>
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following NEW packages will be installed:
  ufw
0 upgraded, 1 newly installed, 0 to remove and 12 not upgraded.
Need to get 287 kB of archives.
...
...
Fetched 287 kB in 1s (477 kB/s)
Selecting previously unselected package ufw.
(Reading database ... 123456 files and directories currently installed.)
Preparing to unpack .../ufw_0.36-7_all.deb ...
Unpacking ufw (0.36-7) ...
...
...
Setting up ufw (0.36-7) ...
...

Default incoming policy changed to 'deny'
Default outgoing policy changed to 'allow'
Rule added
Rule added (v6)
Rule updated
Rule updated (v6)
Firewall is active and enabled on system startup
```

This script configures the firewall to deny all incoming and outgoing traffic by default, then allows specific services such as SSH (for remote access) and HTTP/HTTPS (for web services). It finally enables the firewall rules.
## 3. Filesystems Permissions

Filesystem permissions control access to files and directories on a Linux system. Properly setting these permissions is crucial to limit access to sensitive files and directories, preventing unauthorized users from reading, modifying, or deleting critical data. The `chmod` and `chown` commands are used to modify file permissions and ownership.

Example Script:

```bash
# Set read-write-execute permissions for the owner, read-only for group and others
chmod 644 /path/to/file
# Change the ownership of a directory to a specific user and group
chown username:groupname /path/to/directory
```
Output:
```
>>>
Do you want to perform actions on a file in the current directory? (y/n): 
>>>y
Files in the current directory:
file1.txt
file2.txt
file3.txt

Enter the filename: 
>>>file1.txt
Do you want to (e)ncrypt or (c)hange permissions on the file? (e/c): 
>>>e
File 'file1.txt' encrypted successfully.

#For change of permissions 
>>>c 
Enter the new file permissions:
>>>644
File permissions changed for 'file1.txt' to 644.
```
Service Management is designed such that services which are inactive for a certain time frame are disabled.
User interacts with the GUI for Service Management:

```
>>>
Disabling <service_name> (Inactive for <days_since_activation> days)...
Disabling <another_service_name> (Inactive for <days_since_activation> days)...
...
Disabling <last_service_name> (Inactive for <days_since_activation> days)...
Service management complete.

```

The first command sets the permissions of a file to allow the owner to read, write, and execute it (6), while restricting group and others to read-only (4). The second command changes the ownership of a directory to a specific user and group.

## 4. Service Management

 Service management involves controlling which processes and services are running on your system. Reducing the attack surface means disabling unnecessary services and daemons that could be exploited by attackers. `systemctl` is a command used to manage services in Linux. Disabling services not required for the system's operation helps improve security.
 
 Example Script:
 ```bash
 # Disable a service (e.g., Tor)
sudo systemctl disable tor
# Stop a service (e.g., Tor)
sudo systemctl stop tor
```

Output:

```
>>>
Disabling <service_name> (Inactive for <days_since_activation> days)...
Disabling <another_service_name> (Inactive for <days_since_activation> days)...
...
Disabling <last_service_name> (Inactive for <days_since_activation> days)...
Service management complete.

```

These commands demonstrate how to disable and stop a service (in this case, Tor). Disabling prevents the service from starting automatically during system boot.

## 5. User and Group Management

The principle of least privilege (PoLP) is a security concept that advocates granting users and processes only the minimum permissions necessary to perform their tasks. User and group management involves creating separate user accounts for different purposes, such as administrative tasks and regular usage. This separation helps minimize the potential impact of security breaches.

Example Script:
```bash
# Create a new user
sudo adduser newusername
# Add the user to a specific group
sudo usermod -aG groupname newusername
# Remove a user
sudo deluser username
```
Output:
```
>>>
Creating administrative user account: adminuser
Changing password for user adminuser.
New password:
Retype new password:
passwd: password updated successfully
Adding user `adminuser' to group `sudo' ...
Adding user adminuser to group sudo
Done.

Creating regular user account: regularuser
Changing password for user regularuser.
New password:
Retype new password:
passwd: password updated successfully

Removing default user account: guest
userdel: user 'guest' does not exist
Removing default user account: user1
userdel: user 'user1' does not exist
Removing default user account: user2
userdel: user 'user2' does not exist

Locking unused user account: unuseduser1
passwd: password expiry information changed.
Locking unused user account: unuseduser2
passwd: password expiry information changed.

Cleaning up temporary files
User and group management completed.

```

These commands allow you to create new user accounts, add users to specific groups, and remove user accounts as needed, helping to implement the principle of least privilege by ensuring users have appropriate access rights.


## 6. Password Policies

 Enforcing strong password policies is essential for enhancing system security. Pluggable Authentication Modules (PAM) is a framework used to manage authentication on Linux systems. You can configure PAM to require complex passwords, enforce password expiration, and set other security-related policies. In `pwquality.conf`, you can configure parameters like `minlen` (minimum password length), `minclass` (minimum character classes required), and more.

 Example Script:
 ```bash
 # Install libpam-pwquality for PAM password policies
sudo apt install libpam-pwquality
# Edit the common-password file to enforce password policies
sudo nano /etc/security/pwquality.conf
```

Output:
```
>>>
Reading package lists... Done
Building dependency tree       
Reading state information... Done
libpam-pwquality is already the newest version (1.4.0-9ubuntu2).
libpam-cracklib is already the newest version (1.4.0-9ubuntu2).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
minlen = 12
minclass = 3
maxrepeat = 2
maxsequence = 4
reject_username
enforce_for_root
Password policies have been configured.
```

This script installs the necessary library for PAM password policies and allows you to configure password complexity requirements by editing the `pwquality.conf` file.
## 7. Audit Logging

Audit logging is crucial for monitoring system activities and identifying potentially malicious actions or security breaches. You can enable and configure auditing on Linux systems to log various events and actions. Regularly reviewing these logs is essential for detecting and responding to suspicious behavior.

Example Script:
```bash
# Install auditd for audit logging
sudo apt install auditd
# Enable and start the auditd service
sudo systemctl enable auditd
sudo systemctl start auditd
# View audit logs
sudo ausearch -k KEYWORD
```

Output:
```
>>>
Audit logging has been enabled and configured.
You can review audit logs in /var/log/audit/audit.log.

```

Example of a audit.log file :
```
type=SYSCALL msg=audit(1632717845.012:123): arch=c000003e syscall=2 success=yes exit=3 a0=7fffaa06eb3d a1=0 a2=1 a3=0 items=2 ppid=1234 pid=5678 auid=1000 uid=1000 gid=1000 euid=0 suid=0 fsuid=0 egid=1000 sgid=1000 fsgid=1000 tty=(none) ses=1 comm="open" exe="/usr/bin/cat" key="file_access"

type=CWD msg=audit(1632717845.012:123):  cwd="/home/user/documents"

type=PATH msg=audit(1632717845.012:123): item=0 name="/etc/passwd" inode=12345 dev=08:01 mode=0100644 ouid=0 ogid=0 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0

type=PATH msg=audit(1632717845.012:123): item=1 name="/etc/shadow" inode=54321 dev=08:01 mode=0100400 ouid=0 ogid=0 rdev=00:00 nametype=NORMAL cap_fp=0 cap_fi=0 cap_fe=0 cap_fver=0


```

Replace `KEYWORD` with a specific keyword or event you want to search for in the audit logs. This script installs the auditd package, enables and starts the auditd service, and provides a way to search and review audit logs for specific events.
## 8. File Encryption

File encryption is a method of securing sensitive data by converting its contents into an unreadable format, which can only be decrypted with the appropriate decryption key. The GNU Privacy Guard (GPG) is a commonly used tool for file encryption on Linux systems.

Example Script:
```bash
# Encrypt a file using GPG
gpg --output encrypted_file.gpg --encrypt --recipient recipient@example.com file_to_encrypt.txt
# Decrypt the file
gpg --output decrypted_file.txt --decrypt encrypted_file.gpg
```
You'll need to replace `recipient@example.com` with the recipient's GPG key. This script demonstrates how to encrypt and decrypt a file using GPG. The encrypted file is unreadable without the recipient's private key.
## 9. Port Protection

Port protection in this context refers to disabling USB ports on a Linux system to prevent unauthorized external devices from connecting. This is typically implemented using udev rules that control device access based on attributes like the "authorized" attribute.

Example Script:
To create a udev rule to disable USB ports, you would create a file named `disable-usb.rules` in the `/etc/udev/rules.d/` directory with the following content:
```bash
SUBSYSTEM=="usb", ATTR{authorized}="0"
```
After creating the rule, you need to reload the udev rules using `udevadm control --reload` for it to take effect.
This rule targets USB devices (SUBSYSTEM=="usb") and sets their *authorized* attribute to 0, effectively disabling them.

