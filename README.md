## 1.2 Install with poetry
#### Install only for running project
```
poetry install 
```
#### Install for developing too (Linters included)
```
poetry install --with dev
```


## 1.2 Install with pip
#### Install only for running project
```
pip install -r requirements.txt 
```
#### Install for developing too (Linters included)
```
pip install -r requirements-dev.txt 
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
### 3.2 If installed with pip:
```
python manage.py runserver
```