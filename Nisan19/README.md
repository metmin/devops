# TrendyolSystem Bootcamp Mezuniyet Projesi 1


### Ön Gereksinimler
* Vagrant


### Not:
* Windows Kullanıcılarında Kodların Düzgün Bir Şekilde Çalışabilmesi için aşağıdaki konfigrasyonun yapılması gerekmektedir ( Mac Os ve Linux sistemlerde deneme şansım olmadı :) )
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
* Sanallaştırma için VirtualBox kullanmıyorsanız sunucular ayağa kalktıktan sonra elle disk eklememiz gerekmekte.

* Control Makinesinde `/vagrant/ansible` dizinine geldikten sonra aşağıdaki komutu çalıştıralım:
```
$ ansible-playbook -i hosts playbooks/case1.yml
```

* Localimizde `vagrant ssh case1` komutunu çalıştırarak sunucuya bağlanabilir ve değişiklikleri görebiliriz.

#### Case 1 Aşamaları
* Bu komut ile beraber Ansible, öncelikle sunucudaki güncellemeleri yapar.
* Sonrasında mehmeteminbora kullanıcısı açılıp wheel grubuna bağlanmakta ve sonraki işlemleri mehmeteminbora kullanıcı ile gerçekleştirmektedir.
* Kullanıcı açıldıktan sonra sunucuya bağladığımız diske partition yapıp /mnt/bootcamp dizinine mount eder.
* Sonrasında /opt/bootcamp dizinine bootcamp.txt dosyası açarak içerisine gerekli yazıyı yazar.
* En sonunda da home dizinine geçerek açtığımız dosyayı bulup mount ettiğimiz konuma gönderir. 

### Case 2

* Control Makinesinde `/vagrant/ansible` dizinine geldikten sonra aşağıdaki komutu çalıştıralım:
```
$ ansible-playbook -i hosts playbooks/case2.yml
```

* Ansible işlemleri tamamladıktan sonra `192.168.135.112` adresi üzerinden yayın başlayacaktır.

* `192.168.135.112/user?name=<name>&lastname=<lastname>` ile beraber çağrı atılırsa isim ve soyisim bilgileri veritabanına kaydedilir.

* `192.168.135.112/users` ile beraber çağrı atılırsa veritabanına kaydedilen tüm isim-soyisim bilgilerini ekrana yazdıracaktır.

* `bootcamp=devops` headeri ile beraber çağrı atıldığında `Hoşgeldin Devops` statik sayfasına yönlendirme yapılacaktır.

* Localimizde `vagrant ssh case2` komutunu çalıştırarak sunucuya bağlanabilir ve değişiklikleri görebiliriz.

#### Case 2 Aşamaları

* Bu komut ile beraber Ansible, docker kurulumu için gerekli paketler yüklenir ve docker reposu sisteme eklenir.
* Docker Kurulumu yapılır ve vagrant kullanıcısı docker grubuna eklenir.
* Docker servisi başlatılır ve sunucu yeniden boot edildiğinde açık olması için enable edilir.
* Sonrasında Docker-Compose Kurulumu yapılır.
* En sonunda Docker-Compose kullanılarak hazırlanan Flask-MongoDB-Nginx projesi ayağa kaldırılır.
