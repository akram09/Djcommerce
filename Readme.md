# Djcommerce
Djcommerce is a full e-commerce web application built with the Django framework. built with performance and ease-of-use in mind.
## Current features.
- Home page
- Cart system
- Payment page

### Installation

```bash
git clone https://github.com/akram09/Djcommerce.git
cd Djcommerce
```

if you are using a virtualenv then you need to create a new virtual environment and activate it 

```bash
virtualenv env 
source env/bin/activate
```

then install install the requirement packages 

```bash
pip install -r requirements.txt
```

### Run

```bash
python manage.py makemigration
python manage.py migrate 
python manage.py runserver
```

### Create Admin User 

```bash
python manage.py createsuperuser
```

## Docker Installation

for now the docker compose have only the web container that use simple Sqlite file, I will be adding nginx server and postgres as Db 

```bash
docker-compose build
docker-compose up -d 
```

 
