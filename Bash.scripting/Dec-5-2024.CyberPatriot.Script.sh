#!/bin/bash

# Ask the administrator for the list of authorized users
echo "Enter the list of authorized users (space-separated):"
read -a valid_users

# Function to remove users that are not in the valid list
remove_invalid_users() {
  for user in $(cut -d: -f1 /etc/passwd); do
    if [[ ! " ${valid_users[@]} " =~ " ${user} " ]]; then
      echo "Removing invalid user: $user"
      # Ensure no processes are running before removing the user
      pkill -u $user
      userdel -r $user || echo "Failed to remove user: $user"
    fi
  done
}

# Set up secure password policies
configure_password_policy() {
  # Set minimum length to 10 characters and enforce password expiration
  echo "Setting password policies..."
  echo "PASS_MIN_LEN 10" >> /etc/login.defs
  echo "PASS_MAX_DAYS 30" >> /etc/login.defs
  echo "PASS_MIN_DAYS 7" >> /etc/login.defs
  
  # Expire passwords shorter than 10 characters
  for user in $(cut -d: -f1 /etc/passwd); do
    password_hash=$(passwd -S $user | awk '{print $2}')
    if [[ ${#password_hash} -lt 10 ]]; then
      chage -E 0 $user
    fi
  done

  # Force users with no password to change it
  for user in $(cut -d: -f1 /etc/passwd); do
    if [[ "$(passwd -S $user | awk '{print $2}')" == "NP" ]]; then
      chage -d 0 $user
    fi
  done
}

# Expire passwords that are older than 30 days
expire_old_passwords() {
  echo "Expiring passwords older than 30 days..."
  for user in $(cut -d: -f1 /etc/passwd); do
    last_password_change=$(chage -l $user | grep "Last password change" | awk -F: '{print $2}' | xargs -I {} date -d "{}" +%s)
    current_date=$(date +%s)
    let age_days=($current_date - $last_password_change) / 86400
    if [[ $age_days -gt 30 ]]; then
      echo "Password for user $user is older than 30 days. Expiring password."
      chage -E 0 $user
    fi
  done
}

# Enable UFW and configure default rules
configure_firewall() {
  echo "Enabling UFW firewall..."
  # Ensure UFW is installed
  if ! command -v ufw &>/dev/null; then
    echo "UFW not installed. Installing..."
    apt install -y ufw
  fi
  ufw enable
  ufw default deny incoming
  ufw default allow outgoing
  ufw allow ssh
  systemctl reload ufw
}

# Ensure IPv6 is enabled in UFW default config
check_ipv6_in_ufw() {
  echo "Ensuring IPv6 is enabled in /etc/ufw/defaults..."
  if ! grep -q "IPV6=yes" /etc/ufw/ufw.conf; then
    echo "Enabling IPv6 in UFW..."
    sed -i 's/IPV6=no/IPV6=yes/' /etc/ufw/ufw.conf
    systemctl reload ufw
  fi
}

# Enable automatic updates and set up daily checks
enable_automatic_updates() {
  echo "Enabling automatic updates..."
  apt install -y unattended-upgrades
  dpkg-reconfigure --priority=low unattended-upgrades
  echo "Configuring daily update checks..."
  cat <<EOF > /etc/cron.daily/apt
#!/bin/bash
apt update && apt upgrade -y
EOF
  chmod +x /etc/cron.daily/apt
}

# Disable root SSH login
disable_root_ssh() {
  echo "Disabling root SSH login..."
  sed -i 's/^PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
  systemctl restart sshd
}

# Set the system to reboot after a kernel panic
configure_kernel_panic() {
  echo "Setting system to reboot 10 seconds after a kernel panic..."
  echo "kernel.panic = 10" >> /etc/sysctl.conf
  sysctl -p
}

# Disable IP forwarding
disable_ip_forwarding() {
  echo "Disabling IP forwarding..."
  echo "net.ipv4.ip_forward = 0" >> /etc/sysctl.conf
  sysctl -p
}

# Install and configure ClamAV
install_clamav() {
  echo "Installing ClamAV..."
  apt install -y clamav clamav-daemon
}

# Ask permission to run a clamscan
run clamscan() {
  echo "Would you like to run a clamscan?"
  echo "Enter (y) or (n)"
  read user
  if [ "$user_input" == "y" ]; then
    echo "Updating virus list and running clamscan"
    freshclam
    clamscan -r / --bell -i
}

# Install and configure Chrootkit
install_chrootkit() {
  echo "Installing Chrootkit..."
  apt install -y chrootkit
  chrootkit
}

# Install iptables if not already installed
install_iptables() {
  echo "Checking if iptables is installed..."
  if ! command -v iptables &> /dev/null; then
    echo "Installing iptables..."
    apt install -y iptables
  fi
}

# Remove outdated communication methods
remove_outdated_communications() {
  echo "Removing outdated communication methods..."
  apt remove -y telnet rsh-client
}

# Find file locations of media files and hacking tools
find_media_and_hacking_tools() {
  echo "Searching for media files..."
  find / -type f \( -iname "*.mp3" -o -iname "*.mp4" -o -iname "*.avi" \) > ~/media_files.txt
  echo "Searching for hacking tools..."
  find / -type f \( -iname "*crack*" -o -iname "*hack*" -o -iname "*rootkit*" \) > ~/hacking_tools.txt
}

# Reminder to check startup applications
remind_check_startup() {
  echo "Reminder: Please check your startup applications for any unauthorized programs."
}

# Main function to call all sub-functions
main() {
  remove_invalid_users
  configure_password_policy
  expire_old_passwords
  configure_firewall
  check_ipv6_in_ufw
  enable_automatic_updates
  disable_root_ssh
  configure_kernel_panic
  disable_ip_forwarding
  install_clamav
  install_chrootkit
  install_iptables
  remove_outdated_communications
  find_media_and_hacking_tools
  remind_check_startup
}

# Run the main function
main
