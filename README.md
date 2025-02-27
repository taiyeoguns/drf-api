# DRF-API

Fake data API.

Built with Python and Django Rest Framework.

## Requirements

- Python 3
- [Django Rest Framework](https://www.django-rest-framework.org/) 3.9.x
- [Django](https://www.djangoproject.com/) 5.1.x
- Postgres database

## Installation

### Clone Project

```sh
git clone https://github.com/taiyeoguns/drf-api.git
```

### Install Requirements

With a [virtualenv](https://virtualenv.pypa.io/) already set-up, install the requirements with pip:

```sh
make install
```

### Add details in `.env` file

Create `.env` file from example file and maintain necessary details in it e.g. secret key etc

```sh
cp .env.example .env
```

For deployment to other environments, ensure to maintain the host details in the `.env` file in the `ALLOWED_HOSTS` variable. Similar for `CSRF_TRUSTED_ORIGINS`.

Also set `DEBUG=False` for environments other than development.

### Generate secret key

Generate a secret key to be used by the Django application using the command below:

```sh
python -c "import string,secrets; uni=string.ascii_letters+string.digits+string.punctuation; print(repr(''.join([secrets.choice(uni) for i in range(48)])))"
```

Copy the generated string and add to the `.env` file created in previous step.

### Run migrations

Create tables in the database:

```sh
make db-migrate
```

### Seed database

To populate database with sample data, run:

```sh
make seed
```

`num` parameter specifies how many items to enter into the tables e.g.

```sh
python manage.py seed --num 15
```

### Start the server

Start the Django web server by running:

```sh
make run
```

Open a browser and navigate to `http://localhost:8000/api`

## Documentation

Documentation using OpenAPI is available at `http://localhost:8000/api/docs`

## Tests

In command prompt, run:

```sh
make test
```

### Authentication

To authenticate with the API, appropriate user API token should be passed in the `X-API-KEY` HTTP header, e.g.

```sh
X-API-KEY: 00000000-0000-0000-0000-000000000000
```

In development, if seeding was done, an API token `00000000-0000-0000-0000-000000000000` should exist for use.

Example request:

```sh
curl -X 'GET' \
  'http://localhost:8000/api/employees/' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: 00000000-0000-0000-0000-000000000000'
```

In the OpenAPI (Swagger) documentation page, to authenticate, click on the `Authorize` button before any requests and paste in the token to apply it for all requests needing authentication.

### Run application with Docker

Ensure database details are added to `.env` file from earlier.

The following environment variables should be set in the `.env` file even if they do not 'exist', the docker postgres image will use them for setting up the container -
`POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`

With Docker and Docker Compose set up, run:

```sh
make docker-run
```

Wait till setup is complete and all containers are started.

Thereafter, application should be available at `http://localhost:8000`
