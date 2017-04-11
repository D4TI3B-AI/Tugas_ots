# Peuyeum Framework
Geospatial Web Application Framework

## Requirement
 * virtualenv
 * uwsgi
 * pymongo
 * pycrypto
 * redis

### Instalation
Centos 6 x86_64_ (still on progress)
```sh
# yum --enablerepo=extras install centos-release-SCL
# yum install python27
# cd /etc/yum.repos.d/ 
# wget https://copr.fedorainfracloud.org/coprs/pypa/pypa/repo/epel-6/pypa-pypa-epel-6.repo
# yum clean all
# yum install python-backports
# rpm -ivh ftp://rpmfind.net/linux/centos/6.8/os/x86_64/Packages/python-backports-ssl_match_hostname-3.4.0.2-2.el6.noarch.rpm
# yum install python-pip
# pip install virtualenv
# pip install uwsgi
# pip install pymongo
# pip install pycrypto
# pip install redis
```

Centos 7
```sh
# yum install python-pip python-dev nginx python-MySQLdb
# pip install virtualenv
# pip install uwsgi
```


Ubuntu Installation
```sh
# sudo apt-get install build-essential libssl-dev libffi-dev python-pip python-dev nginx libmysqlclient-dev
# pip install virtualenv
# pip install uwsgi
# pip install MySQL-python
```

### Setup
#### Direktory
Please rename config.py.example to config.py in folder lib, edit configuration as your environment.
```sh
$ cd agenda
$ virtualenv env
$ source env/bin/activate
$ deactivate
```

#### uwsgi
Please edit first peuyeum.ini then edit peuyeum.service; and copy to your operating system service dir

```sh
# cp peuyeum.service /etc/systemd/system/
# systemctl start uwsgi
# systemctl status uwsgi
# systemctl enable uwsgi
```
##### Centos
PLease check selinux for enabling nginx to read socket
```sh
# tail /var/log/audit/audit.log
# getenforce
Enforcing
# setenforce 0
# getenforce
Permissive
# systemctl restart nginx
```
Beware, command above will not work after restart, you must set selinux to enable read socket
```sh
# yum install policycoreutils-python
# grep nginx /var/log/audit/audit.log | audit2allow
# grep nginx /var/log/audit/audit.log | audit2allow -m nginx
# grep nginx /var/log/audit/audit.log | audit2allow -M nginx
# semodule -i nginx.pp
```

#### nginx
This section explain how to run nginx as proxy server of uwsgi edit or create new in /etc/nginx, sites-enables folder of nginx in ubuntu or conf folder of nginx in Centos.

```sh
server {
    listen 80;
    server_name sign.vas.web.id;

    location / {
        include         uwsgi_params;
        uwsgi_pass      unix:/run/uwsgi/signapp.sock;
    }
}
```

#### MongoDB
If your application need mongodb for storing data. please install first rely on your Operating System

##### Centos 7
```sh
# vi /etc/yum.repos.d/mongodb-org.repo
[mongodb-org-3.2]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.2/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.2.asc
# yum repolist
# yum install mongodb-org
# systemctl start mongod
# tail /var/log/mongodb/mongod.log
# mongo
# vi /etc/security/limits.d/20-nproc.conf
…
mongod soft nproc 32000
# systemctl restart mongod
```

Use mongo db run mongo
```sh
> use signapp
> db.sign.insert({NPM:"1234455"})
> db.sign.find()
> quit()
```

#### Redis
If your apps using redis to store TTL Token, please install it to.

##### Centos 7
```sh
# yum install redis
# systemctl enable redis
# systemctl start redis
# systemctl status redis
# redis-cli
```

### How To Use
#### Cilok : Cryptography URI Locator Key
##### URL Format :
 keyuri or tokenuri%controller filename%method inside Controller%paramater
##### Example :
 * For web aplications : WEB%peta%home%2017
 * For API : API%agenda%getList%5101

