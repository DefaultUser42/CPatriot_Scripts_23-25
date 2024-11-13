#!/bin/bash

# Hardening Script for Linux Mint 22
# Written by: ChatGPT (AI Assistant)
# Purpose: Configure and harden a Linux Mint 22 system

# Function to check if the script is running as root
check_root() {
  if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root."
    exit 1
  fi
}

# Function to update the system
update_system() {
  echo -n "Do you want to update your system? [y/N]: "
  read update_choice
  if [[ "$update_choice" =~ ^[Yy]$ ]]; then
    echo "Updating system..."
    apt update && apt upgrade -y && apt dist-upgrade -y
  else
    echo "Skipping system update."
  fi
}

# Function to disable root login via SSH
disable_root_ssh() {
  echo -n "Do you want to disable root login over SSH? [y/N]: "
  read disable_ssh_choice
  if [[ "$disable_ssh_choice" =~ ^[Yy]$ ]]; then
    echo "Disabling root SSH login..."
    sed -i '/^PermitRootLogin/s/.*/PermitRootLogin no/' /etc/ssh/sshd_config
    systemctl restart ssh
  else
    echo "Leaving root login enabled over SSH."
  fi
}

# Function to configure a basic firewall (ufw)
configure_firewall() {
  echo -n "Do you want to configure UFW firewall? [y/N]: "
  read ufw_choice
  if [[ "$ufw_choice" =~ ^[Yy]$ ]]; then
    echo "Setting up UFW firewall..."
    ufw allow OpenSSH
    ufw enable
    echo "Firewall configured and enabled."
  else
    echo "Skipping UFW firewall configuration."
  fi
}

# Function to install fail2ban for SSH protection
install_fail2ban() {
  echo -n "Do you want to install fail2ban for SSH protection? [y/N]: "
  read fail2ban_choice
  if [[ "$fail2ban_choice" =~ ^[Yy]$ ]]; then
    echo "Installing fail2ban..."
    apt install fail2ban -y
    systemctl enable fail2ban
    systemctl start fail2ban
    echo "fail2ban installed and started."
  else
    echo "Skipping fail2ban installation."
  fi
}

# Function to configure automatic security updates
configure_security_updates() {
  echo -n "Do you want to enable automatic security updates? [y/N]: "
  read auto_update_choice
  if [[ "$auto_update_choice" =~ ^[Yy]$ ]]; then
    echo "Configuring automatic security updates..."
    apt install unattended-upgrades -y
    dpkg-reconfigure --priority=low unattended-upgrades
  else
    echo "Skipping automatic updates configuration."
  fi
}

# Function to configure logging and auditd
setup_auditd() {
  echo -n "Do you want to install and configure auditd for logging? [y/N]: "
  read audit_choice
  if [[ "$audit_choice" =~ ^[Yy]$ ]]; then
    echo "Installing auditd..."
    apt install auditd -y
    systemctl enable auditd
    systemctl start auditd
    echo "auditd installed and configured."
  else
    echo "Skipping auditd installation."
  fi
}

# Function to configure password policy (PAM)
configure_password_policy() {
  echo -n "Do you want to enforce strong password policies? [y/N]: "
  read password_choice
  if [[ "$password_choice" =~ ^[Yy]$ ]]; then
    echo "Enforcing password policy..."
    sed -i 's/^#minlen = 8/minlen = 12/' /etc/security/pwquality.conf
    sed -i 's/^#minclass = 3/minclass = 4/' /etc/security/pwquality.conf
    echo "Password policy configured to require at least 12 characters and 4 character classes."
  else
    echo "Skipping password policy configuration."
  fi
}

# Function to disable unnecessary services
disable_unnecessary_services() {
  echo -n "Do you want to disable unnecessary services (e.g., Bluetooth, CUPS)? [y/N]: "
  read disable_services_choice
  if [[ "$disable_services_choice" =~ ^[Yy]$ ]]; then
    echo "Disabling unnecessary services..."
    systemctl disable bluetooth.service
    systemctl stop bluetooth.service
    systemctl disable cups.service
    systemctl stop cups.service
    echo "Unnecessary services disabled."
  else
    echo "Skipping disabling unnecessary services."
  fi
}

# Function to remove unused packages
remove_unused_packages() {
  echo -n "Do you want to remove unused packages? [y/N]: "
  read remove_packages_choice
  if [[ "$remove_packages_choice" =~ ^[Yy]$ ]]; then
    echo "Removing unused packages..."
    apt autoremove --purge -y
    apt clean
    echo "Unused packages removed."
  else
    echo "Skipping removal of unused packages."
  fi
}

# Main function to run all tasks
main() {
  check_root

  echo "Starting system hardening..."
  update_system
  disable_root_ssh
  configure_firewall
  install_fail2ban
  configure_security_updates
  setup_auditd
  configure_password_policy
  disable_unnecessary_services
  remove_unused_packages

  echo "System hardening complete!"
}

# Run the main function
main
