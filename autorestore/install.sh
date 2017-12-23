#! /bin/bash

# Install required packages ---------------------------------------------------
apt update
apt-get -y upgrade
apt-get -y install kate git libinput10 xserver-xorg-input-libinput screen nano gedit python chromium-browser guake gitk build-essential vlc gimp make okular

# Call the setup script -------------------------------------------------------
./setup.py
