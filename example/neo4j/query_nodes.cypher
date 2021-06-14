USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///reporting_tables.csv" AS csvLine
CREATE (:Reporting {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()});
USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///analytics_tables.csv" AS csvLine
CREATE (:Analytics {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()});
USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///github_repos_tables.csv" AS csvLine
CREATE (:GitHub_Repos {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()});
