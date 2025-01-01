#!/bin/bash

# Configurations
ALLOWED_USERS_FILE="/home/secure_admin/Desktop/allowed_users.txt"  # Path to the allowed users file
PASSWORD_AGE_MIN=30                               # Minimum password age in days
PASSWORD_AGE_MAX=90                               # Maximum password age in days
MIN_PASSWORD_LENGTH=10                            # Minimum password length

# List of system users to exclude from deletion (can be expanded if needed)
SYSTEM_USERS=("root" "daemon" "bin" "sys" "sync" "games" "man" "lp" "mail" "news" "uucp" "proxy" "www-data" "backup" "list" "irc" "_apt" "nobody" "systemd-network" "systemd-timesync" "dhcpcd" "messagebus" "syslog" "systemd-resolve" "polkitd" "usbmux" "tss" "rtkit" "systemd-coredump" "kernoops" "uuidd" "cups-pk-helper" "avahi-autoipd" "_flatpak" "avahi" "geoclue" "dnsmasq" "nm-openvpn" "lightdm" "tcpdump" "speech-dispatcher" "fwupd-refresh" "cups-browsed" "saned" "hplip" "colord" "sssd")

# Ensure allowed users file exists
if [[ ! -f "$ALLOWED_USERS_FILE" ]]; then
    echo "Allowed users file does not exist: $ALLOWED_USERS_FILE"
    exit 1
fi

# Read the allowed users into an array
mapfile -t allowed_users < "$ALLOWED_USERS_FILE"

# Check each system user
for user in $(cut -d: -f1 /etc/passwd); do
    # Skip system users (i.e., users with a UID below 1000 are typically system users)
    user_uid=$(id -u "$user")
    if [[ $user_uid -lt 1000 ]]; then
        echo "Skipping system user $user (UID: $user_uid)."
        continue
    fi

    # Check if the user is in the allowed list
    if [[ ! " ${allowed_users[@]} " =~ " $user " ]]; then
        # Skip essential system users
        if [[ " ${SYSTEM_USERS[@]} " =~ " $user " ]]; then
            echo "Skipping essential system user $user."
            continue
        fi

        # Ask for user input before deleting
        read -p "User '$user' is not in the allowed list. Do you want to delete this user account (and home directory)? (y/n): " confirm
        if [[ "$confirm" =~ ^[Yy]$ ]]; then
            echo "Deleting user $user..."

            # Delete the user account (and optionally remove their home directory)
            sudo userdel -r "$user"
            
            if [[ $? -eq 0 ]]; then
                echo "User $user has been successfully deleted."
            else
                echo "Failed to delete user $user."
            fi
        else
            echo "User $user deletion canceled."
        fi
        continue
    fi

    # Check password age
    password_last_changed=$(chage -l "$user" | grep 'Last password change' | cut -d: -f2)
    if [[ -n "$password_last_changed" ]]; then
        # Convert the last password change date to seconds since epoch
        last_change_sec=$(date -d "$password_last_changed" +%s)
        current_date_sec=$(date +%s)
        password_age_days=$(( (current_date_sec - last_change_sec) / 86400 ))  # Calculate password age in days
        
        # Check if the password age is within the allowed range
        if (( password_age_days < PASSWORD_AGE_MIN )); then
            echo "User $user has a password that was changed less than $PASSWORD_AGE_MIN days ago. Consider waiting longer before changing it."
        elif (( password_age_days > PASSWORD_AGE_MAX )); then
            echo "User $user has a password older than $PASSWORD_AGE_MAX days. The password needs to be changed."
        else
            echo "User $user has a valid password age ($password_age_days days)."
        fi
    else
        echo "Could not retrieve password change date for user $user. Skipping password age check."
    fi

    # Check if the password meets the minimum length requirement
    shadow_entry=$(sudo getent shadow "$user")
    password_hash=$(echo "$shadow_entry" | cut -d: -f2)

    if [[ ${#password_hash} -lt $MIN_PASSWORD_LENGTH ]]; then
        echo "User $user has a password that is too short. Minimum length required is $MIN_PASSWORD_LENGTH characters."
    else
        echo "User $user has a password that meets the minimum length."
    fi

done

echo "User account management script completed."
