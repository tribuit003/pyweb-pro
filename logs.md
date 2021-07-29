
Cài đặt
https://docs.docker.com/samples/django/

https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script

https://docs.docker.com/compose/install/

sudo docker-compose run web django-admin startproject sourcecode .
sudo chown -R $USER:$USER .

# Commnad to use in Python Django
python manage.py migrate
python manage.py createsuperuser

# Command to login database
psql -U postgres
\dt
SELECT * FROM xxx;
Ctrl+L to Clear Screen

# Import
requests