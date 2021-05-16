# sqlquerygraph
[![build status](https://github.com/avisionh/sqlquerygraph/workflows/pytesting/badge.svg)](https://github.com/avisionh/sqlqueryraph/actions) [![CodeFactor](https://www.codefactor.io/repository/github/avisionh/sqlquerygraph/badge)](https://www.codefactor.io/repository/github/avisionh/sqlquerygraph) [![License: MIT](https://img.shields.io/badge/License-MIT-informational.svg)](https://opensource.org/licenses/MIT) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Parse your SQL queries and represent their structure as a graph.

## Requirements
To run the code in here, ensure your system meets the following requirements:
- Unix-like operating system (macOS, Linux, ...);
- [`direnv`](https://direnv.net/) installed, including shell hooks;
- [`.envrc`](https://github.com/avisionh/sqlquerygraph/blob/main/.envrc) allowed/trusted by `direnv` to
  use the environment variables - see [below](#allowingtrusting-envrc);
- Python 3.8 or above; and
- [Poetry](https://python-poetry.org/docs/) installed.

Parse your SQL queries and represent their structure as a graph.

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

***
