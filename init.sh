sudo ln -sf /home/fedor/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/fedor/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo gunicorn -c /etc/gunicorn.d/hello.py hello:application
sudo /etc/init.d/gunicorn restart
