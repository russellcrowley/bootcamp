#!/bin/sh
# this script is the standalone installer for a twitter scraping script using twint
# to run:
# chmod +x twint_script_installer.sh
# sudo ./twint_script_installer.sh

# install dependencies for twint - pip3 and lolcat
apt-get update
apt install python3-pip -y
apt install lolcat -y
# install twint from github repo, and associated requirements
git clone https://github.com/twintproject/twint.git
cd twint
pip3 install . -r requirements.txt
# go back up a directory to keep twint installation separate
cd ..
# get twint script from github and execute it
wget https://raw.githubusercontent.com/russellcrowley/bootcamp/main/twint_script.sh
chmod +x twint_script.sh
./twint_script.sh 
