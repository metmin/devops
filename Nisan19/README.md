# TrendyolSystem Bootcamp Mezuniyet Projesi 1


### Ön Gereksinimler
* Vagrant

### Not:
* Windows Kullanıcılarında Kodların Düzgün Bir Şekilde Çalışabilmesi için aşağıdaki konfigrasyonun yapılması gerekmektedir (Mac Os ve Linux sistemlerde deneme şansım olmadı :))
```
$ git config --global core.autocrlf false
```

## Başlangıç
* Öncelikle Projeyi Klonlayalım
* `vagrant up` komutu ile makinelerimizi ayağa kaldıralım.
* Sanallaştırma için VirtualBox kullanılırsa Vagrant otomatik olarak ilk case de diski bağlayacaktır.
* Kurulum bittikten sonra `vagrant ssh control` komutu ile ansible kullanacağımız makineye girelim.
* `cd /vagrant/ansible` komutu ile beraber ansible kodlarımızın olduğu dizine gelelim.


### Case 1

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

### Case 2

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
