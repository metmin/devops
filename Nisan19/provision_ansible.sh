#!/bin/bash
echo "Starting provisioning of Ansible..."

sudo apt-get update
sudo apt-get autoremove -y
sudo apt-add-repository -y ppa:ansible/ansible
sudo apt-get install -y ansible=2.9.6+dfsg-1 \
    software-properties-common \
    python3-setuptools \
    python3-dev \
    git \
    python3-pip
pip3 install "yamllint==1.25.0" "ansible-lint==4.3.7"