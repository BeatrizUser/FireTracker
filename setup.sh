# Atualiza database do repositorio
apt update

# Instala dependencias
apt install -y sqlite
<<<<<<< HEAD

# Roda migrations
python3 manage.py migrate

# Cria superuser
python3 manage.py createsuperuser --username admin

# Inicia
python manage.py makemigrations
python manage.py migrate
=======
    
>>>>>>> 8553b66 (repair 1)
