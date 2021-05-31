# enter docker neo4j instance
docker exec -it neo4j bash

# move .csv files into import/ folder for loading into neo4j
mv data/*csv import/

# pipe content of .cypher file into cypher-shell
cat data/example_import.cypher | bin/cypher-shell --username $NEO4J_USERNAME --password $NEO4J_PASSWORD --format plain
