ARG PY_VER=3.8.0
FROM python:${PY_VER} AS sqlqeurygraph-py

# build requirements
COPY ./wait-for-it.sh ./
COPY ./neo4j ./

RUN mkdir /app \
        && mkdir /import \
        && mkdir /data \
        && pip install py2neo \
        && chmod +x /wait-for-it.sh \
        #&& /wait-for-it.sh neo4j:7687

COPY neo4j/*csv import/
COPY neo4j/*cypher data/
COPY ./loader.py .

CMD ["wait-for-it.sh", "neo4j:7687","loader.py", "data/query_constraints.cypher"]
ENTRYPOINT ["python3"]
