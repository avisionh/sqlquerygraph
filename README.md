# sqlquerygraph
[![build status](https://github.com/avisionh/sqlquerygraph/workflows/pytesting/badge.svg)](https://github.com/avisionh/sqlqueryraph/actions)
[![](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![CodeFactor](https://www.codefactor.io/repository/github/avisionh/sqlquerygraph/badge)](https://www.codefactor.io/repository/github/avisionh/sqlquerygraph)
[![License: MIT](https://img.shields.io/badge/License-MIT-informational.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Parse your SQL queries and represent their structure as a graph.

Currently, we implement the ability of representing how each of the tables in a set of SQL query scripts depend on each other.

## Requirements
To run the code in here, ensure your system meets the following requirements:
- Unix-like operating system (macOS, Linux, ...);
- [`direnv`](https://direnv.net/) installed, including shell hooks;
- [`.envrc`](https://github.com/avisionh/sqlquerygraph/blob/main/.envrc) allowed/trusted by `direnv` to
  use the environment variables - see [below](#allowingtrusting-envrc);
- Python 3.8 or above; and
- [Poetry](https://python-poetry.org/docs/) installed.

Note there may be some Python IDE-specific requirements around loading environment variables, which are not considered here.

### Set-up
For quickstart set-up of the project, run the below in your shell:
```shell script
# 1. read project-specific environment variables
direnv allow

# 2. activate virtual environment and install package dependencies
poetry shell
poetry install

# 3. check adherence to good standards on every commit
pre-commit install
```

### Run neo4j graph database
We use [neo4j](https://neo4j.com/) for this project to visualise the dependencies between tables. To install neo4j locally using Docker Compose, follow the below instructions:
1. Install Docker
    + For Mac OSX, install Docker and Docker Compose together [here](https://docs.docker.com/docker-for-mac/install/).
    + For Linux, install Docker [here](https://docs.docker.com/engine/install/) and then follow these [instructions](https://docs.docker.com/compose/install/) to install docker-compose.
    + For Windows, install Docker and Docker Compose together [here](https://docs.docker.com/docker-for-windows/install/).
1. Within this directory that has the `docker-compose.yml` file, run the below in your shell/terminal:
    ```shell script
    docker-compose up -d
    ```
1. If it's the first time you have downloaded the neo4j docker image, wait awhile (maybe an hour, depends on your machine specs). If you have downloaded the neo4j docker image before (such as going through these instructions), then wait a few minutes. Then launch neo4j locally via opening your web browser and entering the following web address:
    - http://localhost:7474/browser/
1. The default username and password will be:
   ```
   username: neo4j
   password: neo4j
   ```
   You can leave the other fields blank. neo4j will then prompt you to change your password. Change it to whatever you please.

***

## Acknowledgements
This builds on the excellent [moz-sql-parser](https://github.com/mozilla/moz-sql-parser) package.
