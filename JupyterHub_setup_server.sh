#!/usr/bin/bash
# Ubuntu 20.04.6 LTS

set -e

apt update
apt upgrade -y
timedatectl set-timezone America/Chicago

# install mambaforge and needed packages
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh -b -p /opt/mambaforge # has mamba 1.4.2, conda 23.3.1, python 3.10
export PATH=/opt/mambaforge/bin:/opt/mambaforge/condabin:$PATH
mamba init -y
mamba update mamba -y # got 1.5.0
mamba install anaconda -c anaconda -y # appears to be 2022.10 versions; mamba now 1.4.9
mamba install altair vega_datasets vega jupyterhub nbgrader oauthenticator -y # jupyterhub 4.0.2; nbgrader 0.8.2

# get JupyterHub config file
cd /opt/mambaforge/etc/jupyter
wget https://raw.githubusercontent.com/TLU-Physics/TLU-JupyterHub/main/jupyterhub_config.py


# Setup for nbgrader for 2 classes

mkdir -p /usr/local/share/nbgrader/exchange
chmod ugo+rw /usr/local/share/nbgrader/exchange

mkdir /etc/jupyter
cd /etc/jupyter
wget https://raw.githubusercontent.com/TLU-Physics/TLU-JupyterHub/main/nbgrader_config-etc.py
mv nbgrader_config-etc.py nbgrader_config.py
adduser grader-coursephys371 --gecos "" --disabled-password --force-badname
adduser grader-coursephys241l --gecos "" --disabled-password --force-badname

cd /home/grader-coursephys371
sudo -u grader-coursephys371 /opt/mambaforge/bin/nbgrader quickstart coursePHYS371
sudo -u grader-coursephys371 mkdir .jupyter
cd .jupyter
sudo -u grader-coursephys371 wget https://raw.githubusercontent.com/TLU-Physics/TLU-JupyterHub/main/nbgrader_config-phys371.py
sudo -u grader-coursephys371 mv nbgrader_config-phys371.py ./nbgrader_config.py

cd /home/grader-coursephys241l
sudo -u grader-coursephys241l /opt/mambaforge/bin/nbgrader quickstart coursePHYS241L
sudo -u grader-coursephys241l mkdir .jupyter
cd .jupyter
sudo -u grader-coursephys241l wget https://raw.githubusercontent.com/TLU-Physics/TLU-JupyterHub/main/nbgrader_config-phys241l.py
sudo -u grader-coursephys241l mv nbgrader_config-phys241l.py ./nbgrader_config.py

cd /usr/local/share
mkdir jupyter
cd jupyter
echo "" > nbgrader.log
chmod 666 nbgrader.log

# create various user directories
adduser tsauncy@tlu.edu --gecos "" --disabled-password --force-badname
adduser stud1@tlu.edu --gecos "" --disabled-password --force-badname
adduser aarcsalinas@tlu.edu --gecos "" --disabled-password --force-badname
adduser ajsilva@tlu.edu --gecos "" --disabled-password --force-badname
adduser hhernandez@tlu.edu --gecos "" --disabled-password --force-badname
adduser adrimartinez@tlu.edu --gecos "" --disabled-password --force-badname
adduser tmharrison@tlu.edu --gecos "" --disabled-password --force-badname
adduser jasacastro@tlu.edu --gecos "" --disabled-password --force-badname

./configure_nbgrader_extensions.sh
