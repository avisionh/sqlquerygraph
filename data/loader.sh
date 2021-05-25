# enter docker neo4j instance
docker exec -it neo4j bash
cypher-shell --username $NEO4J_USERNAME --pasword $NEO4J_PASSWORD

# use default neo4j database
:use neo4j

# run cypher code

# exit cypher shell
:exit
