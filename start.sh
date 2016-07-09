#!/bin/bash
 apt-get update && apt-get -y upgrade
 apt-get -y install apache2 python-pip libapache2-mod-wsgi
 apt-get install debconf-utils
 export DEBIAN_FRONTEND=noninteractive
 apt-get -y install mysql-server-5.5 --fix-missing
 apt-get -y install virtualenv --fix-missing
cd /opt/
virtualenv django-env
cd django-env
. bin/activate
sudo pip install django
django-admin startproject kkidb
cat > /etc/apache2/conf-available/kkidb.conf <<EOF
WSGIScriptAlias / /opt/django-env/kkidb/kkidb/wsgi.py
WSGIPythonPath /opt/django-env/kkidb:/opt/django-env/lib/python2.7/site-packages

<Directory /opt/django-env/kkidb>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
EOF

sudo pip install django
sudo apt-get install python-mysqldb
sudo a2enconf kkidb
sudo systemctl restart apache2.service 

cd kkidb
python manage.py startapp polls
cd ..
sudo cp -f -r /../../kkidb_static/* kkidb/

sudo mysql < kkidb/datainit.sql

echo 'I HAVE BEEN SUMMONED!'