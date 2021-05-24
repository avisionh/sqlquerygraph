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
