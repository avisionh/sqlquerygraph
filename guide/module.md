### Module arguments

In the Python module example run to extract and export to `.csv` the table names and dependencies of `.sql` scripts:
```shell script
python sqlquerygraph.py -sd 'sql' -ed 'neo4j' -rd 'github_repos' 'analytics' 'reporting'
```
More arguments can be specified to provide greater customisation. They are:

| Argument - short | Argument - long | Description | Required |
|------------------|-----------------|-------------| -------- |
| `-sd` | `--script_dir` | Directory where we store subdirectories of our SQL queries. | True |
| `-d`     | `--sub_dir` | Subdirectories within script_dir that you want to read SQL queries from. If no value is inputted, then use all subdirectories in script_dir. | False |
| `-rd` | `--reference_datasets` | Datasets that contain tables in database to look-up against. | True |
| `-ed` | `--export_dir` | Directory to store files. | True |
| `-v` | `--verbose` | Boolean to output steps taken and query after cleaning. Useful if want to check where function is failing. If no value is inputted, then it is False. " | False |

### Accessing Docker container terminal
To access the bash terminal in the Docker container and the Cypher shell in there:

```shell script
# access Docker container terminal
docker exec -it neo4j bash

# access Cypher shell
cypher-shell --username $NEO4J_USERNAME --password $NEO4J_PASSWORD

# use default neo4j db
:use neo4j

# run some cypher commands

# exit neo4j db
:exit
```
