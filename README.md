# django-python-test2

Используется СУБД PostgreSQL:

Создать базу:

`sudo -u postgres psql`  
`CREATE DATABASE mysite2;`  
`CREATE USER mysite2user WITH PASSWORD 'password';`  

Установки кодировки, Уровень изоляции(Данные доступны для чтения после подтверждения транзакции), Временная зона:

`ALTER ROLE mysite2user SET client_encoding TO 'utf8';`  
`ALTER ROLE mysite2user SET default_transaction_isolation TO 'read committed';`  
`ALTER ROLE mysite2user SET timezone TO 'UTC';`  

Привилегии пользователю:

`GRANT ALL PRIVILEGES ON DATABASE mysite2 TO mysite2user;`  

`\q`

Настройки подключения к базе:

`DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  
        'NAME': 'mysite2',  
        'USER': 'mysite2user',  
        'PASSWORD': 'password',  
        'HOST': 'localhost',  
        'PORT': '',  
    }  
}  
`  

Выполнение миграции:

`python3 manage.py migrate` 

Публичная часть - `movies/`

