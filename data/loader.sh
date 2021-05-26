# enter docker neo4j instance
docker exec -it neo4j bash

# move .csv files into import/ folder
mv data/*csv import/

# access cypher shell
cypher-shell --username $NEO4J_USERNAME --pasword $NEO4J_PASSWORD

# use default neo4j database
:use neo4j

# run cypher code

# exit cypher shell
:exit
