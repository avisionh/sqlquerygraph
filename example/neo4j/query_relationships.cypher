USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///reporting_analytics_dependency.csv" AS csvLine
MERGE (a:Reporting {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})
MERGE (b:Analytics {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})
CREATE (a)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(b);
USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///reporting_github_repos_dependency.csv" AS csvLine
MERGE (a:Reporting {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})
MERGE (b:GitHub_Repos {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})
CREATE (a)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(b);
USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///analytics_analytics_dependency.csv" AS csvLine
MERGE (a:Analytics {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})
MERGE (b:Analytics {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})
CREATE (a)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(b);
USING PERIODIC COMMIT 500 LOAD CSV WITH HEADERS FROM "file:///analytics_github_repos_dependency.csv" AS csvLine
MERGE (a:Analytics {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})
MERGE (b:GitHub_Repos {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})
CREATE (a)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(b);
