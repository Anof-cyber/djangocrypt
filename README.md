# djangocrypt
A test app for PyCript Burp Extension


## Requirements

- Pytohn 3.7+

## Installation

### Docker

```bash

## Installation
docker build -t djangocrypt .    

## Run Web Server
docker run -p 8000:8000 djangocrypt 
```



#### Windows
```bash

## Installation
git clone https://github.com/Anof-cyber/djangocrypt
cd djangocrypt
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

## Run Web Server
cd djangocrypt
venv\Scripts\activate
Python djangocrypt\manage.py runserver
```

#### Linux
```bash

## Installation
git clone https://github.com/Anof-cyber/djangocrypt
cd djangocrypt
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Run Web Server
cd djangocrypt
source venv/bin/activate
Python djangocrypt/manage.py runserver
```

Access the http://127.0.0.1:8000/


