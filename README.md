## 0. Prerequisites
### 0.1 Installing python:

Download python and install it from official site https://www.python.org/

### 0.2 Cloning git repository:
```
git clone https://github.com/h4x4d/intensive_django.git
```
### 0.3 Going to folder:
```
cd intensive_django
```

### 0.4 If you want to use venv
```
pip install virtualenv
virtualenv env
```
Windows:
```
.\venv\Scripts\activate
```
Linux:
```
source venv/bin/activate
```

## 1. Fast run project (Install all dependencies and run):
```
make use
```

## 1.1 Install with poetry (you also need to install poetry to use it)
#### Install only for running project
```
poetry install 
```
Make shortcut:
```
make install
```
#### Install for developing too (Linters included)
```
poetry install --with dev
```
Make shortcut:
```
make install-dev
```


## 1.2 Install with pip (ready to use with default python)
#### Install only for running project
```
pip install -r requirements.txt 
```
Make shortcut:
```
make pip-install
```
#### Install for developing too (Linters included)
```
pip install -r requirements-dev.txt 
```
Make shortcut:
```
make pip-install-dev
```

## 2. Configuring .env

### 2.1 Adding access_key, for example:
```
SECRET_KEY=AYDFHIJUOAIKPLDFFDbi[o]
```
### 2.2 Checking debug status: 1 - on; 2 - off:
```
DEBUG=1
```
### 2.3 Adding allowed hosts, for example:
```
ALLOWED_HOSTS=127.0.0.1;11.11.11.11
```

## 3. Running project
### 3.1 If installed with poetry:
```
poetry run python manage.py runserver
```
Make shortcut:
```
make run
```
### 3.2 If installed with pip:
```
python manage.py runserver
```
Make shortcut:
```
make pip-run
```