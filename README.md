# Library Project

Instructions for setting up the project.

![coverage](./coverage.svg)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)
## Quickstart

Clone the project in your development environment

```shell script
git clone https://github.com/hugobrilhante/work-at-olist.git
```

Enter the project folder and download and install the dependencies

> Note: Assuming you have [pipenv](https://github.com/pypa/pipenv#installation),  [docker](https://docs.docker.com/install/), [docker-compose](https://docs.docker.com/compose/install/) and [nodejs](https://nodejs.org/en/download/)  installed


```shell script
cd work-at-olist
make setup
```

## Useful commands

```shell script
make setup: Installs development dependencies, creates database and run project.

make up: Start project in daemon.

make stop: Stop project services.

make test: Run tests
```


## Environment

* Computer: Macbook pro 13'
* Os: macOS Catalina
* IDE: PyCharm

## Library

#### Tests and Code Style

* autopep8
* autoflake
* flake8
* isort
* pytest-django
* pytest-cov
* pytest-factoryboy

#### Application and docs

* django 2.2.12 (LTS)
* django-configurations
* djangorestframework
* django-filter
* drf-yasg
* gunicorn
* psycopg2
* whitenoise

> Note: I used a django template that I made recently to use in my projects [beatsolu/django-templates](https://github.com/beatsolu/django-templates)


## Application Example

[https://work-at-olist](https://work-at-olist-hugobrilhante.herokuapp.com/)

#### Credentials
    login: admin
    password: admin



