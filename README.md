# Library

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

make up: Starts project in daemon.

make stop: Stop project services.

make test: Run tests
```
