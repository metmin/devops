# TrendyolSystem Bootcamp Mezuniyet Projesi 2 Database Case

### Ön Gereksinimler
* Vagrant (test için kullanılan makineler vagrant ile açılıp yapılandırıldı, dilerseniz kendiniz de iki makine açıp devam edebilirsiniz ancak Api için kurulumları yapacağımız makinenin CentOs olması gerekmekte).


### Not:
* Windows Kullanıcılarında Kodların Düzgün Bir Şekilde Çalışabilmesi için aşağıdaki konfigrasyonun yapılması gerekmektedir ( Mac Os ve Linux sistemlerde deneme şansım olmadı :) )
```
$ git config --global core.autocrlf false
```


## Başlangıç
* Öncelikle Projeyi Klonlayalım
* `vagrant up` komutu ile makinelerimizi ayağa kaldıralım.
* Vagrant ile beraber couchbase kuracağımız sunucuya docker otomatik olarak yüklü gelecektir.


### Case-1 Couchbase Kurulumu 
* Vagrant kurulumları bittikten sonra `vagrant ssh db` komutu ile couhbase kuracağımız makineye girelim.

* Aşağıdaki komutlar ile beraber couchbase makinelerimizi ayağa kaldıralım.
```
$ docker run -d -p 8091:8091 --name db1 couchbase/server-sandbox:6.6.0
$ docker run -d -p 9091:8091 --name db2 couchbase/server-sandbox:6.6.0
```

* Localimizde `http://192.168.135.112:8091/` adresine girerek ayağa kalkan makinelerimizden birini görebiliriz (diğer makinemiz de 9091 portunda çalışmakta).

* Not-1: (Eğer projedeki Vagrantfile ile kurulum yapmadıysanız ip adresi değişebilir).

* Not-2: Makinemize yeni bir node ekleme ve rebalance konuları Case-2' de işlenecektir.

### Case-2 Python Modülü 
* Couchbase makinelerimizde işimiz bittikten sonra makineden çıkarak `vagrant ssh api` ile beraber Api kuracağımız makineye bağlanalım.

* Projemizde Flask kullanacağız ve bunu localimizde test etmek için de venv (Virtual Environment) kullanıcam.

* Öncelikle gerekli yum paketlerini indirelim
```
$ sudo yum install centos-release-scl -y
$ sudo yum install rh-python36 -y
```

* Sonrasında da python3 paketini aşağıdaki komut ile enable edelim.
```
$ scl enable rh-python36 bash
```

* Kullanıcımızın home dizinine flaskapi diye bir klasör oluşturalım ve bu proje ile beraber gelen api.py dosyasını bu klasöre atalım.
```
$ mkdir ~/flaskapi
$ cp /vagrant/app.y ~/flaskapi/app.py
```

* flaskapi klasörümüze girelim ve venv kurulumu yapalım.
```
$ cd ~/flaskapi
$ python3 -m venv venv
```

* Virtual Environment' imizi aktif edelim ve gerekli Pip paketlerinin kurulumlarını yapalım.
```
$ source venv/bin/activate
$ pip install Flask
$ pip install requests
```

* Apimizi ayağa kaldırmak için hazırız. Aşağıdaki komut ile beraber çalıştıralım.
```
$ flask run -h 0.0.0.0
```

* Tarayıcımızda `http://192.168.135.113:5000/` adresine girerek Api' mize bağlanabiliriz (Eğer projedeki Vagrantfile ile kurulum yapmadıysanız ip adresi değişebilir).

## Kullanılabilir komutlar

* `/add_node?ip=<node_adresi>&username=<Node_Kullanıcı_Adı>&password=<Node_Şifresi>&services=<servisler>` ekleyerek host makinemize yeni Node' lar ekleyebiliriz. Örnek:
```
$ http://192.168.135.113:5000/add_node?ip=172.17.0.3&username=Administrator&password=password&services=kv,n1ql
```
* Not: Host Containeri ilk defa ayağa kalktığında localhost ile çalışmaya başlıyor ve node ekleme işlemi yapıldığında önce kendi IP Adresini 172 ile başlayan bir adrese güncelliyor. Bu durumda yukarıdaki komutu çalıştırdığımızda hata verebilir. Host makinesi IP Adresini güncelleyip yeniden ayağa kalktığında yukarıdaki komutu bir daha çalıştırmamız gerekmekte.

* `/rebalance` ile beraber rebalance işlemi başlatabiliriz.


* `/pools` ile beraber sistemimizin ve node'ların özelliklerini görebiliriz


* `/pools/node_list` ile beraber sistemimizdeki Node ların listesini görebiliriz.


* `/pools/nodes_info` ile beraber sistemimizdeki Node ların özelliklerini görebiliriz.
