# sqlquerygraph
[![build status](https://github.com/avisionh/sqlquerygraph/workflows/pytesting/badge.svg)](https://github.com/avisionh/sqlqueryraph/actions)
[![codecov](https://codecov.io/gh/avisionh/sqlquerygraph/branch/main/graph/badge.svg?token=8TD296ECEE)](https://codecov.io/gh/avisionh/sqlquerygraph)
[![](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![CodeFactor](https://www.codefactor.io/repository/github/avisionh/sqlquerygraph/badge)](https://www.codefactor.io/repository/github/avisionh/sqlquerygraph)
[![License: MIT](https://img.shields.io/badge/License-MIT-informational.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Parse your SQL queries and represent their structure as a graph.

Currently, we implement the ability of representing how each of the tables in a set of SQL query scripts depend on each other.

```cypher
MATCH p=(r:Reporting)-[:HAS_TABLE_DEPENDENCY]->()-[:HAS_TABLE_DEPENDENCY]->()
WHERE r.table_name='user_activity'
RETURN p
```
![](./guide/img/table_dependency.png)

## Requirements
To run the code in here, ensure your system meets the following requirements:
- Unix-like operating system (macOS, Linux, ...) - though it might work on Windows;
- Python 3.8 or above; and
- [Poetry](https://python-poetry.org/docs/) installed.
- [`direnv`](https://direnv.net/) installed, including shell hooks;

<!--Note there may be some Python IDE-specific requirements around loading environment variables, which are not considered here. -->

### Set-up
For quickstart set-up of the project, run the below in your shell/terminal:
```shell script
# 1. read project-specific environment variables
direnv allow

# 2. activate virtual environment and install package dependencies
poetry shell
poetry install

# 3. check adherence to good standards on every commit
pre-commit install
```

To then extract the tables and their dependencies from the example SQL scripts in the `sql/` directory, run the below in your shell/terminal. It will generate `.csv` files of the tables and their dependencies. It will also generate `.cypher` files to enable you to import the data into neo4j, after you have added the `.csv` files to the database.
```shell script
python sqlquerygraph.py -sd 'sql' -ed 'neo4j' -rd '<datasets, individually quoted and separated by commas, of tables in sql/ scripts>'
```

### Run neo4j graph database
We use [neo4j](https://neo4j.com/) for this project to visualise the dependencies between tables. To install neo4j locally using Docker Compose, follow the below instructions:
1. Install and open Docker (if already installed, just open the program).
    + For Mac OSX, install Docker and Docker Compose together [here](https://docs.docker.com/docker-for-mac/install/).
    + For Linux, install Docker [here](https://docs.docker.com/engine/install/) and then follow these [instructions](https://docs.docker.com/compose/install/) to install docker-compose.
    + For Windows, install Docker and Docker Compose together [here](https://docs.docker.com/docker-for-windows/install/).

1. Create a new file, `.secrets`, in the directory where this `README.md` file sits, and store the following in there. This allows you to set the password for your local neo4j instance without exposing it.
   ```
   export NEO4J_AUTH=neo4j/<your_password>
   export NEO4J_USERNAME=neo4j
   export NEO4J_PASSWORD=<your_password>
   ```
   Then update your `.env` file to take in the new `.secrets` file you created by entering the below in your shell/terminal:
   ```shell script
   direnv allow
   ```

1. Build the Docker image and launch the container. Within this directory that has the `docker-compose.yml` file, run the below in your shell/terminal:
   ```shell script
   docker-compose up
   ```
   You will know when it's ready when you get the following message in your terminal:
   ```
   app      | [INFO  wait] Host [neo4j:7687] is now available!
   app      | [INFO  wait] --------------------------------------------------------
   app      | [INFO  wait] docker-compose-wait - Everything's fine, the application can now start!
   app      | [INFO  wait] --------------------------------------------------------
   ```
   Then launch neo4j locally via opening your web browser and entering the following web address:
    - http://localhost:7474/

   The username and password will those specified in your `.secrets` file.

1. When you have finished playing with your local neo4j instance, remember to stop it running by executing the below in your shell/terminal:
   ```shell script
   docker-compose down
   # option if you want to delete data too
   docker-compose down --volumes
   ```

***

## Acknowledgements
This builds on the excellent [moz-sql-parser](https://github.com/mozilla/moz-sql-parser) package.

With thanks also to the [Google Cloud Public Dataset Program](https://cloud.google.com/solutions/datasets) for which the SQL queries in this repo are based off the program's [GitHub repos](https://console.cloud.google.com/marketplace/product/github/github-repos) dataset.
