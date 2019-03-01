# DRF-API

Fake data API.

Built with Python and Django Rest Framework.

## Requirements

- Python 3
- [Django Rest Framework](https://www.django-rest-framework.org/) 3.9.x
- [Django](https://www.djangoproject.com/) 2.1.x

## Installation

### Clone Project

```sh
git clone https://github.com/taiyeoguns/drf-api.git
```

### Install Requirements

With a [virtualenv](https://virtualenv.pypa.io/) already set-up, install the requirements with pip:

```sh
pip install -r requirements.txt
```

### Run migrations

Create tables in the database:

```sh
python manage.py migrate
```

### Seed database

To populate database with sample data, run:

```sh
python manage.py seed
```

`num` parameter specifies how many items to enter into the tables e.g.

```sh
python manage.py seed --num 15
```

### Start the server

Start the Django web server by running:

```sh
python manage.py runserver
```
