#!/bin/sh
echo "-----------------------------------------------------------"
echo "will install all for the IBS project"
echo "-----------------------------------------------------------"
#SUBLIME
if which "subl" >/dev/null; then
    echo "sublime 3 exists"
else
    echo "Installing: sublime 3"
    sudo add-apt-repository ppa:webupd8team/sublime-text-3
    sudo apt-get update
    sudo apt-get install sublime-text-installer
fi

echo "-----------------------------------------------------------"
#CURL
if which "curl" >/dev/null; then
    echo "curl exists"
else
    echo "Installing: curl"
   	sudo apt-get install curl
fi

echo "-----------------------------------------------------------"
#PYCHARM
#http://linuxg.net/how-to-install-pycharm-3-1-on-ubuntu-linux-mint-and-elementary-os/
if which "pycharm" >/dev/null; then
    echo "pycharm exists"
else
    echo "Installing: pycharm"
   	wget -q -O - http://archive.getdeb.net/getdeb-archive.key | sudo apt-key add -
	sudo sh -c 'echo "deb http://archive.getdeb.net/ubuntu trusty-getdeb apps" >> /etc/apt/sources.list.d/getdeb.list'
	sudo apt-get update
	sudo apt-get install pycharm
fi

echo "-----------------------------------------------------------"
#NGINX
if which "nginx" >/dev/null; then
    echo "nginx exists"
else
    echo "Installing: nginx"
	sudo apt-get install nginx
fi



echo "-----------------------------------------------------------"
echo "git configure"
echo "-----------------------------------------------------------"
rep="car"

echo "-----------------------------------------------------------"
#PIP
if which "pip" >/dev/null; then
    echo "pip exists"
else
	echo "Installing: pip"
    sudo apt-get install python-pip
fi

echo "-----------------------------------------------------------"
#VIRTUALENV
if which "virtualenv" >/dev/null; then
    echo "virtualenv exists"
else
	echo "Installing: virtualenv"
    sudo pip install virtualenv
fi

echo "-----------------------------------------------------------"
#GIT
if which "git" >/dev/null; then
    echo "git exists"
else
	echo "Installing: GIT"
    sudo apt-get install git
fi

echo "-----------------------------------------------------------"
echo "Installing: "

if [ -d ~/repositories ]; then
  	echo "~/repositories allready exists!"
else
	echo "creating ~/repositories"
	mkdir ~/repositories
fi

cd ~/repositories

if [ -d ~/repositories/$rep ]; then
  	echo "~/repositories/$rep allready exists!"
else
	echo "creating ~/repositories/$rep"
	#mkdir ~/repositories/$rep
	git clone https://github.com/vovacooper/car
fi

cd car





echo "-----------------------------------------------------------"
echo "Virtualenv configure"
echo "-----------------------------------------------------------"

#VIRTUALENV
if [ -d ~/repositories/$rep/bin ]; then
  	echo "virtualENV exists!"
else
	echo "creating virtualENV"
	#mkdir ~/repositories/$rep
	virtualenv .
fi

source bin/activate
#deactivate

echo "It seems like your system does not have gcc. 
Install build tools using following command: 
apt-get install build-essential python-dev"
sudo apt-get install build-essential python-dev 

#install openssl for uwsgi websocket
sudo apt-get install libssl-dev

echo "installing all requairments for repository"
./bin/pip install -r req.txt --upgrade  --force-reinstall


echo "-----------------------------------------------------------"
echo "UWSGI configuration"
echo "-----------------------------------------------------------"

#sudo service uwsgi restart
#sudo service nginx restart
echo "DONE"
echo "-----------------------------------------------------------"

exit