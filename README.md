# Django Playground

## Installation
Create a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Make migrations:

```sh
python manage.py makemigrations
python manage.py migrate
```

## Generating data

```sh
python seed.py
```

## Running the project

```sh
python manage.py runserver
```

## Deactivate using venv

```sh
deactivate
```