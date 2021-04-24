# Vagrant Ansible Lab

The lab will implement the following configuration:

-
| Machine  Name | Role          | Network Configuration                  | OS                         |
|---------------|---------------|----------------------------------------|----------------------------|
| control       | Ansible  host | private_network, ip: 192.168.135.10    | Ubuntu Focal64 (20 LTS)   |
| app01         | web server 1  | private_network, ip: 192.168.135.111   | Ubuntu Focal64 (20 LTS)   |
| app02         | web server 2  | private_network, ip: 192.168.135.112   | Centos 7   |


## Prerequisites
* Install the Vagrant 2.2.15 from https://www.vagrantup.com/downloads
* Install the Virtualbox 6.1.18 from https://www.virtualbox.org/wiki/Downloads if it is not installed already.
* Download the Vagrant boxes for your preferred hypervisor:
  ```
  $ vagrant box add centos/7
  $ vagrant box add ubuntu/focal64
  ```

## Quick Start
* Clone this repo
* Ensure you have installed Vagrant and Virtualbox(check `Prerequisites` section)
* Run `vagrant up` from the root of the cloned repo (the folder with Vagrantfile in it)
* Once the VMs are built, type `vagrant ssh control` to login to the ansible controller from within your vagrant project folder.
* Change directories `cd /vagrant/ansible` which is the ansible subfolder of your vagrant project for this lab (the vagrant project folder is mounted within the VMs as /vagrant during provisioning)

## Important Files
* [./hosts](ansible/hosts): File defining the servers to be managed
* [./ansible.cfg](ansible/ansible.cfg): Ansible supports several sources for configuring its behavior, including an ini file named [ansible.cfg](ansible.cfg), environment variables, command-line options, playbook keywords, and variables. Changes can be made and used in a configuration file which will be searched for in the following order(Ansible will process the below list and use the first file found, all others are ignored.):
  - `ANSIBLE_CONFIG` (environment variable if set)
  - `ansible.cfg` (in the current directory)
  - `~/.ansible.cfg` (in the home directory)
  - `/etc/ansible/ansible.cfg`
* [./group_vars/all/main.yml](ansible/group_vars/all/main.yml): Global variables file for all of the host groups
* [./group_vars/nginx/main.yml](ansible/group_vars/nginx/main.yml): Global variables file for `nginx` host group
* [./group_vars/prometheus/main.yml](ansible/group_vars/prometheus/main.yml): Global variables file for `prometheus` host group
* [./playbooks](ansible/playbooks): Playbook folder for Ansible lab
* [./roles](ansible/roles): Role folder for Ansible lab

## Examples

### Working With Inventory

List all hosts:
```
$ ansible --list-hosts all
$ ansible --list-hosts "*"
```

List hosts from specific group:
```
$ ansible --list-hosts loadbalancer
```

List hosts using wildcard filter
```
$ ansible --list-hosts "app*"
```

List hosts from multiple groups
```
$ ansible --list-hosts database,control
```

List first node in webserver group:
```
$ ansible --list-hosts webserver[0]
```

List hosts not in control group:
```
$ ansible --list-hosts \!control
```

### Adhoc Command Examples

Ping all of the hosts:
```
$ ansible -m ping all
```

Run `hostname` command on target hosts:
```
$ ansible -m command -a "hostname" all
```

Run `hostname` command on target hosts(here we are not passing module, `command` module is the default one):
```
$ ansible -a "hostname" all
```

### Playbook Examples

Simple playbook that executes "hostname" command:
```shell
$ ansible-playbook -i /vagrant/ansible/hosts /vagrant/ansible/playbooks/hostname.yml
```

Show what hosts are involved in this playbook:
```
$ ansible-playbook -i /vagrant/ansible/hosts /vagrant/ansible/playbooks/hostname.yml --list-hosts
```

Show what tags are involved in this playbook:
```
$ ansible-playbook -i /vagrant/ansible/hosts /vagrant/ansible/playbooks/hostname.yml --list-tags
```

Run only steps in a playbook that have a tag called "packages" defined:
```shell
$ ansible-playbook -i /vagrant/ansible/hosts /vagrant/ansible/playbooks/site.yml --tags "packages"
```

Run only steps in a playbook that DON'T have a tag called "packages" defined:
```
$ ansible-playbook -i /vagrant/ansible/hosts /vagrant/ansible/playbooks/site.yml --skip-tags "packages"
```

Step through tasks and be prompted whether to run each step or not:
```
$ ansible-playbook -i /vagrant/ansible/hosts /vagrant/ansible/playbooks/site.yml --step
```

Show all tasks that will be executed by the playbook:
```
$ ansible-playbook -i /vagrant/ansible/hosts /vagrant/ansible/playbooks/site.yml --list-tasks
```

Skip over steps in a playbook and start at a specific task:
```
$ ansible-playbook -i /vagrant/ansible/hosts /vagrant/ansible/playbooks/stack_status.yml --start-at-task "verify end-to-end response"
```

Verify syntax:
```
$ ansible-playbook --syntax-check /vagrant/ansible/playbooks/site.yml
```

Do a simulated run of the playbook:
```
$ ansible-playbook --check -i /vagrant/ansible/hosts /vagrant/ansible/playbooks/site.yml
```
