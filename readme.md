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

### Add details in `.env` file

Create `.env` file from example file and maintain necessary details in it e.g. secret key etc

```sh
cp .env.example .env
```

### Generate secret key

Generate a secret key to be used by the Django application using the command below:

```sh
python -c "import string,secrets; uni=string.ascii_letters+string.digits+string.punctuation; print(repr(''.join([secrets.choice(uni) for i in range(48)])))"
```

Copy the generated string and add to the `.env` file created in previous step.

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

Open a browser and navigate to `http://localhost:8000/api`

## Documentation

Documentation using OpenAPI is available at `http://localhost:8000/api/docs`

## Tests

In command prompt, run:

```sh
pytest
```
