# enter docker neo4j instance
docker exec -it sqlquerygraph_neo4j_1 bash
cypher-shell -u neo4j -p ${NEO4J_PASSWORD}

# run cypher code

# exit cypher shell
:exit
