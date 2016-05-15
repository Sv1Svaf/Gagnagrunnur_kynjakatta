#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
apt-get update && apt-get -y upgrade
apt-get -y install apache2 python3-pip libapache2-mod-wsgi-py3 mysql-server-5.5 virtualenv python3-virtualenv
update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
update-alternatives --install /usr/bin/python python /usr/bin/python3.4 2
cd /opt/
virtualenv -p /usr/bin/python django-env
cd django-env
. bin/activate
pip install django
django-admin startproject kkidb
cat > /etc/apache2/conf-available/kkidb.conf <<EOF
WSGIScriptAlias / /opt/django-env/kkidb/kkidb/wsgi.py
WSGIPythonPath /opt/django-env/kkidb:/opt/django-env/lib/python3.4/site-packages

<Directory /opt/django-env/kkidb>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
EOF

a2enconf kkidb
systemctl restart apache2.service 
