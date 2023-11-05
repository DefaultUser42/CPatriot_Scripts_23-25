#!/bin/bash
# You may have to use chmod to modify the credentials of this file before executing.
# Navigate to the directory that houses this file and run 'chmod -x CyberPatriot.script.1.sh' to give executable permissions to this file.
sudo

echo "This is a program that is supposed to harden the Linux kernel (To a certain degree.)"

# Update and upgrade the system
echo "Would you like to update and upgrade the system? (y or n)"
read updateandupgrade
while [ $updateandupgrade == "y" ]; do
    echo "Updating and Upgrading the system"
    apt update -y
    script apt upgrade -y
    break
done

# Installs clamav
echo "Would you like to install clamav? (y or n)"
read installclamav
while [ $installclamav == "y" ]; do
    echo "Installing clamav"
    script apt install clamscan
    break
done

# Installs unattended-upgrades
echo "Would you like to set up automatic updates? (y or n)"
read installunattended
while [ $installunattended == "y" ]; do
    echo "Setting up automatic updates"
    apt install unattended-upgrades
    break
done

# Opens gedit to set the minimum password length to 10
echo "Would you like to open gedit to set the minimum password length to 10? (y or n)"
read minpasslen
while [ $minpasslen == "y" ]; do
    echo "Opening gedit to change the min pass length"
    echo "Add a section after this line -> 'password        [success=1 default=ignore]      pam_unix.so obscure sha512' that says 'minlen = 10'" 
    sudo gedit /etc/pam.d/common-password
    break
done

# Tells the user how to set a maximum password age
echo "Would you like to know how to edit the max password age? (Doesn't actually do it)(y or n)"
read maxpassage
while [ $maxpassage == "y" ]; do
    echo "Use the command 'sudo chage -l username' to check the status of a password age for a given user."
    echo "Use the command 'sudo chage username' to manually change the password age for a given user."
    echo "Note: You have to do this individually for each user."
    break
done

# Checks for unwanted files such as mp3's and mp4's
echo "Would you like to check for unwanted files like .mp3's and .mp4's? (y or n)"
read searchunwanted
while [ $searchunwanted == "y" ]; do
    echo "Searching for unwanted files"
    find / -type f -name "*.mp3"
    find / -type f -name "*.mp4"
    find / -type f -name "*.jpg"
    find / -type f -name "*.jpeg"
    find / -type f -name "*.png"
    find / -type f -name "*.webm"
    echo "Use the following command to delete by filetype: 'find / -type f -iname \*.jpg -delete'"
    break
done 

# Retrieves the status of the /etc/passwd and /etc/shadow files
echo "Would you like to check the properties of the /etc/shadow and /etc/passwd files? (y or n)"
read proppass
while [ $proppass == "y" ]; do
    echo "Retrieving the status info for /etc/shadow"
    stat /etc/shadow
    echo "Retrieving the status info for /etc/passwd"
    stat /etc/passwd
    break
done

# Checks the sudoers file for errors
echo "Would you like to check the sudoers file? (y or n)"
read sudoers
while [ $sudoers == "y" ]; do
    echo "cat'ing the sudoers file"
    cat /etc/sudoers
    break
done

# Installs chkrootkit
echo "Would you like to install chkrootkit? (y or n)"
read installchkrootkit
while [ $installchkrootkit == "y" ]; do
    sudo apt install chkrootkit
    break
done

# Opens gedit to edit the chkrootkit config file to run daily. 
echo "Would you like to edit chkrootkit config file to run daily? (y or n)"
read geditchkrootkit
while [ $geditchkrootkit == "y" ]; do
    echo "Change the portion that says RUN_DAILY=”false” to RUN_DAILY=”true”"
    gedit /etc/chkrootkit.conf
    break
done

# Disables SSH root access
echo "Would you like to disable root SSH acces? (y or n)"
read rootssh
while [ $rootssh == "y" ]; do
    echo "Uncomment the line that says #PermitRootLogin prohibit-password and replace prohibit-password with 'no'"
    gedit /etc/ssh/sshd_config
    break
done

# Gives information about how to restrict SSH access
echo "Consider using the 'who | grep username  (to get the pts/# terminal) && sudo pkill -f pts/#' commands to break any existing SSH connections that removed users may still have."
echo ""
echo "Also consider using this command 'AllowGroups sshlogin' to make a group that has access to SSH'ing in order to manually restrict access to users that should have this kind of access."
echo ""
echo "In order to add users, you have to use the first command. The second one just restarts the service after the users have been added."
echo ""
echo "'sudo adduser username sshlogin' 'sudo systemctl restart sshd.service'"
read -p "Press enter to continue"
echo ""
echo "As well, take a look at this site? https://pc-freak.net/blog/how-to-make-sure-your-linux-system-users-wont-hide-or-delete-their-bash_history-securing-bash_history-file/."
read -p "Press enter to continue"
echo ""

# Opens gedit in order to change the default SSH port
echo "Note: Changing the default SSH port limits the risk of an automated attack."
echo ""
echo "Would you like to change the default ssh port (Recomended by People)(y or n)"
read defaultsshport
while [ $defaultsshport == "y" ]; do
    echo "Just add a line that says 'Port 7645' or something similar and make sure that that port is not blocked in the firewall"
    gedit /etc/sshd/sshd_config
    break
done

# Restarts sshd service after the previous command
echo "Would you like to restart sshd (y or n)"
read restartsshd
while [ $restartsshd == "y" ]; do
    echo "Restarting sshd"
    service sshd restart
    break
done

# Checks existing rules in iptables
echo "Would you like to check for existing rules in iptables? (y or n)"
read checkiptables
while [ $checkiptables == "y" ]; do
    echo "Checking rules"
    sudo iptables -L
    break
done

# Installs iptables if not already
echo "Would you like to install iptables? (y or n)"
read installiptables
while [ $installiptables == "y" ]; do
    echo "Installing iptables"
    apt install iptables -y
    break
done

# Sets iptables rules
echo "Would you like to configure iptables using standard settings? (y or n)"
read confiptables
while [ $confiptables == "y" ]; do
    echo "Configuring iptables"
    iptables -P INPUT DROP
    iptables -P OUTPUT ACCEPT
    iptables -P FORWARD REJECT
    break
done

# Checks the iptables rules to make sure that they were set using the last step
echo "Would you like to make sure that the last step worked? (y or n)"
read checkiptables
while [ $checkiptables == "y" ]; do
    echo "Checking rules"
    sudo iptables -L
    break
done

# Appends iptables rules
echo "Would you like to append the iptables rules that you just set? (y or n)"
read appendiptables
while [ $appendiptables == "y" ]; do
    echo "Appending iptables"
    iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
    iptables -A OUTPUT -m conntrack --ctstate ESTABLISHED -j ACCEPT
    break
done

# Allows loopback connections (Some applications may not work.)
echo "Would you like to allow loopback connections? (P.S. Some applications may not work.)(y or n)"
read loopbackconnections
while [ $loopbackconnections == "y" ]; do
    echo "Allowing loopback connections"
    iptables -A INPUT -i lo -j ACCEPT
    iptables -A OUTPUT -o lo -j ACCEPT
    break 
done

# Allows permissive range with iptables
echo "Would you like to apply permissive policy using iptables? (y or n)"
read permissivepolicy
while [ $permissivepolicy == "y" ]; do
    echo "Enter iptables -P INPUT ACCEPT && iptables -P OUTPUT ACCEPT as well as iptables -P FORWARD DROP && iptables -A INPUT -p tcp --dport 22 -m iprange --src-range 192.168.1.100-192.168.1.110 -j REJECT "
    echo "I didn't code this function in because it was too complicated to code this instead of just doing it this way."
    echo ""
    echo "You can also block specific ports with TCP using the following command 'iptables -A INPUT -p tcp --destination-port 22 -j DROP"
    echo ""
    break
done

# Saves the previous iptables modifications to the rules file
echo "Note: IPTABLES RULES ARE NOT PERSISTENT AND WILL NOT BE RESTORED AFTER A REBOOT"
echo "Would you like to save the previous commands? (y or n)"
read saveiptables
while [ $saveiptables == "y" ]; do
    echo "Saving configuration for iptables"
    echo ""
    echo "When the gedit window opens up, check to see that all of the rules have been properly applied."
    sudo  iptables-save > /etc/iptables.up.rules
    gedit /etc/network/if-pre-up.d/iptables
    break
done

# Gives the previous file execution permissions
echo "Would you like to give the file that you made in the last command execution permissions? (y or n)"
read executepermiss
while [ $executepermiss == "y" ]; do
    echo "Giving the iptables rules file execution permissions."
    chmod +x /etc/network/if-pre-up.d/iptables
    break
done

# Info on how to remove iptables rules
echo "Would you like to remove all of the rules for iptables (Doesn't actually do it)(y or n)?"
read useless
while [ $useless == "y" ]; do
    echo "Use the following command to remove the rules for iptables: 'sudo iptables -F'"
    break
done

# Info on how to remove one iptable rule
echo "Would you like to undo a singular rule for iptables? (Doesn't actually do it)(y or n)"
read undosingle
while [ $undosingle == "y" ]; do
    echo "Use the following command to remove a single rule from iptables: 'sudo iptables -F INPUT'"
    break
done

# Info on how to enable IDS
echo "Consider looking into how to set up an IDS"
echo ""
echo "This is a useful link regarding SNORT which is made by Cisco: https://linuxhint.com/snort-ubuntu-tutorial/"
read -p "Press enter to continue"
echo ""

# Info on drive encryption
echo "Consider looking into how to encrypt drives"
echo ""
read -p "Press enter to continue"

# Removing apparmor as a precursor to enabling SELinux
echo "In order to enable SELinux, you first have to stop, disable, and remove apparmor entirely. The following command will do everything up to the installation of SELinux. The following command will also reboot the system after deleting apparmor."
echo ""
echo "Would you like to remove AppArmor as a precursor to installing SELinux? (y or n)"
read rmapparmor
while [ $rmapparmor == "y" ]; do
    echo "stopping, disabling, and removing apparmor. HINT: Will reboot afterward."
    sudo systemctl stop apparmor
    systemctl status apparmor
    sudo systemctl disable apparmor
    sudo apt-get remove apparmor -y
    sudo reboot
    break
done

# Installs SELinux and its' dependancies
echo "Would you like to install SELinux? (y or n)"
read installselinux
while [ $installselinux == "y" ]; do
    echo "Installing SELinux and its' dependancies."
    sudo apt-get install policycoreutils selinux-utils selinux-basics -y
    sudo selinux-activate
    break
done

# Sets SELinux to enforcing
echo ""
echo "The following command will reboot the system following completion."
echo ""
echo "Would you like to set SELinux to enforcing? (y or n)"
read enforceselinux
while [ $enforceselinux == "y" ]; do
    echo "Setting SELinux to enforcing."
    sudo selinux-config-enforcing
    sudo reboot
    break
done

# Checks the status of SELinux
echo "Would you like to check the status of SELinux (y or n)"
read statselinux
while [ $statselinux == "y" ]; do
    echo "Checking the status of SELinux"
    setstatus
    break
done

# Views the log file for SELinux
echo "Would you like to view the log file for SELinux? (y or n)"
read logselinux
while [ $logselinux == "y" ]; do
    echo "Retrieving the log file for SELinux"
    grep selinux /var/log/audit/audit.log
    break
done

# View the status of AppArmor
echo "Would you like to view the status of AppArmor (If still installed)(y or n)"
read statapparmor
while [ $statapparmor == "y" ]; do
    echo "Viewing the status of AppArmor"
    sudo apparmor_status
    break
done

# Install AppArmor if not already installed
echo "Would you like to install AppArmor? (y or n)"
read installapparmor
while [ $installapparmor == "y" ]; do
    echo "Installing AppArmor"
    sudo apt install apparmor-profiles
    break
done

# Info on AppArmor profiles
echo ""
echo "The following information came from this site: https://ubuntu.com/server/docs/security-apparmor."
echo ""
echo "Apparmor makes profiles for every application that is installed on the system, each profile can either be set to complain mode or enforce."
echo ""
echo "There are two modes for apparmor profiles, which are complain and enforce. Complain only logs violations, while enforce actually does something about them."
echo ""
echo "The next two commands will enable either of the two modes, only one can be enabled at a time. "
echo ""
read -p "Press enter to continue"
echo ""

echo "sudo aa-complain /path/to/bin"
echo ""
echo "sudo aa-enforce /path/to/bin"
echo ""
read -p "Press enter to continue"
echo ""

echo "'sudo apparmor_status' is used to check the status of an AppArmor profile. To place all profiles into complain mode, use the following command:"
echo ""
echo "sudo aa-complain /etc/apparmor.d/*"
echo ""
read -p "Press enter to continue"
echo ""

echo "To place all profiles into enforce mode, use the following command: "
echo ""
echo "sudo aa-enforce /etc/apparmor.d/*"
echo ""
read -p "Press enter to continue"
echo ""

echo "The following command is used to reload all profiles:"
echo ""
echo "sudo systemctl reload apparmor.service"
echo ""
read -p "Press enter to continue"
echo ""

echo "apparmor_parser is used to load a profile into the kernel. It can also be used to reload a currently loaded profile using the -r option after modifying it to have the changes take effect. To reload a profile:"

echo "sudo apparmor_parser -r /etc/apparmor.d/profile.name"
echo ""
read -p "Press enter to continue"
echo ""
echo "End of script, there are links to other hardening scripts and other stuff in the .txt doc that should be bundled with this."
echo ""
read -p "Press enter to terminate"
exit
