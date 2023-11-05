## Try using a loop to ask for a users input and then break once their input matches a certain value. 

#!/bin/bash

echo "Would you like to update and upgrade the system? (y or n)"
read updateandupgrade

if [ "$updateandupgrade" == "y" ]; then
    echo "Updating and Upgrading the system"
    apt update -y
    apt upgrade -y
elif [ "$updateandupgrade" == "n" ]; then
    echo "Would you like to install Uncomplicated firewall?"
    read installufw

    if [ "$installufw" == "y" ]; then
        if [ "$FIREWALL" = true ]; then
            echo "Installing Uncomplicated firewall"
            apt-get install ufw -y
        fi
    else
        echo "Finished"
    fi
else
    echo "Finished 3"
fi

echo "Finished 2"