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

​	or you can do it manually by going to the /accounts/signup