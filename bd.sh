sudo /etc/init.d/mysql start
mysql -uroot -e "create database aq1"
sudo pip3 install django
source web/bin/activate
python3 web/ask/manage.py makemigrations qa
python3 web/ask/manage.py migrate

