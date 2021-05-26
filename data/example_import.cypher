// Create constraints on table_name property to ensure each label has unique table_name
CREATE CONSTRAINT table_name_ConstraintReporting ON (r:Reporting)
ASSERT r.table_name IS UNIQUE;
CREATE CONSTRAINT table_name_ConstraintAnalytics ON (a:Analytics)
ASSERT a.table_name IS UNIQUE;
CREATE CONSTRAINT table_name_ConstraintRaw ON (g:GithubRepos)
ASSERT g.table_name IS UNIQUE;

// Create table nodes to join later
LOAD CSV WITH HEADERS FROM "file:///reporting_tables.csv" AS csvLine
CREATE (:Reporting {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()});

LOAD CSV WITH HEADERS FROM "file:///analytics_tables.csv" AS csvLine
CREATE (:Analytics {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()});

LOAD CSV WITH HEADERS FROM "https:file:///github_repos_tables.csv" AS csvLine
CREATE (:GithubRepos {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset), import_datetime: datetime()});

// Load table dependency data
LOAD CSV WITH HEADERS FROM "file:///reporting_analytics_dependency.csv" AS csvLine
MERGE (r:Reporting {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})
MERGE (a:Analytics {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})
CREATE (r)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(a);
LOAD CSV WITH HEADERS FROM "file:///reporting_github_repos_dependency.csv" AS csvLine
MERGE (r:Reporting {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})
MERGE (g:GithubRepos {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})
CREATE (r)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(g);

LOAD CSV WITH HEADERS FROM "file:///analytics_analytics_dependency.csv" AS csvLine
MERGE (a1:Analytics {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})
MERGE (a2:Analytics {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})
CREATE (a1)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(a2);
LOAD CSV WITH HEADERS FROM "file:///analytics_github_repos_dependency.csv" AS csvLine
MERGE (a:Analytics {table_name: toString(csvLine.table_name), table_dataset: toString(csvLine.table_dataset)})
MERGE (g:GithubRepos {table_name: toString(csvLine.dependency_name), table_dataset: toString(csvLine.dependency_dataset)})
CREATE (a)-[:HAS_TABLE_DEPENDENCY {import_datetime: datetime()}]->(g);
