
# GUI Based Hardening of Organisational Security Policies

Enhance OS security through intuitive hardening procedures compliant with organizational policies, prioritizing user experience and interface

With features such as Patch Management,Port Protection,Firewall Configuration Management,SSH Hardening,Filesystem Permissions,Service Management,User and Group Management,Password Policies,Audit Logging,etc. 


## Features

- Patch Managemement: Keep the system up to date by applying security updates and patches regularly.
    - Implemented with `apt` package manager

-  Firewall Configuration: Configure the firewall to restrict incoming and outgoing network traffic. Only allow necessary services and ports, and deny all others.
     - Implemented with `ufw` utility software

     

-  SSH Hardening: To enhance SSH service security, disable root login, implement strong key-based authentication, limit login attempts, and if possible, disable password-based authentication for added protection.
     - Implemented by modifying the SSH server configuration file (sshd_config).

- Port Protection: Disables USB ports on a Linux system to prevent external devices from getting access.
     - Implemented by creating a `udev` rule file named `disable-usb.rules` in the `/etc/udev/rules.d/ directory`. This rule disables all USB devices by setting their authorized attribute to 0.

- Filesystem Permissions:  Review and set appropriate filesystem permissions to limit access to sensitive files and directories.
     - Implemented by using the `chmod` and `chown` command

- Service Management: Disable unnecessary services and daemons to reduce the attack surface, to manage services and only enable those required for the system's operation.
     - Implemented by using `systemctl` command. 

- User and Group Management: Implement the principle of least privilege. Create separate user accounts for administrative tasks and regular usage.Remove or lock default and unused user accounts.
     - Implemented with `ufw` utility software

- Password Policies: Enforce strong password policies using tools like Pluggable Authentication Modules (PAM). Require complex passwords and set password expiration
     - Implemented with `ufw` utility software

-File Encryption : 

- Audit Logging: Enable and configure audit logging to monitor system activities and detect suspicious behavior.
     - Implemented with `ufw` utility software

- DDos prevention: There are multiple sub features in this feature such as 
    - Rate Limiting 
    - Intrusion Detection Systems (IDS) 
    - Intrusion Prevention Systems (IPS)
    - Web Application Firewalls 
    - DNS Protection


