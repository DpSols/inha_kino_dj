# NESMI Django API

## Project setup

* [Python 3.9.2](https://www.python.org/downloads/release/python-392/).
* [pip](https://pip.pypa.io/en/stable/installing/)
* [Virtuelenv](https://pypi.org/project/virtualenv/)


### Clone repo
```
git clone https://github.com/JollyGoal/inha_kino_dj.git
cd inha_kino_dj
```

### Setting up virtuelenv
```
virtualenv venv
```

#### Windows
```
venv\Scripts\activate
```

#### Linux
```
source venv/bin/activate
```

### Install dependencies
```
pip install -r requirements.txt
```

### Apply All database changes

```
python manage.py makemigrations
python manage.py migrate
```

### Create Admin Account
```
python manage.py createsuperuser
```

### Run server
```
python manage.py runserver
```


