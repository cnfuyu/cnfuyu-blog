#!/bin/bash
#@author:cnfuyu<cnfuyu@gmail.com>

#update
apt-get update

#install libs
apt-get install -y zlib1g zlib1g-dev
apt-get install -y openssl libssl-dev
apt-get install -y libpcre3 libpcre3-dev

#install nginx
apt-get install -y nginx

#install uwsgi
apt-get install -y uwsgi

#indicate we use python
apt-get install -y uwsgi-plugin-python

#install pip
apt-get install -y python-pip

#git
apt-get install -y git

#install virtualenv
apt-get install -y python-virtualenv

#pyenv folder
if [ ! -d "/home/pyenv" ]; then
    mkdir /home/pyenv
fi

cd /home/pyenv

virtualenv cnfuyu-blog;

. cnfuyu-blog/bin/activate;

#work folder
if [ ! -d "/home/work" ]; then
    mkdir /home/work
fi

cd /home/work

#TODO username
git clone https://github.com/cnfuyu/cnfuyu-blog.git

cd /home/work/cnfuyu-blog

#install dependences
pip install -r requirements.txt

#configure nginx
cp ./conf/cnfuyu_blog_nginx /etc/nginx/sites-available
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/cnfuyu_blog_nginx /etc/nginx/sites-enabled/cnfuyu_blog_nginx

#configure uwsgi
cp ./conf/cnfuyu_blog_uwsgi.ini /etc/uwsgi/apps-available
ln -s /etc/uwsgi/apps-available/cnfuyu_blog_uwsgi.ini /etc/uwsgi/apps-enabled/cnfuyu_blog_uwsgi.ini

#remove
rm -r ./conf

#chown
chown www-data:www-data -R /home/work

#restart service 
service nginx restart
service uwsgi restart
