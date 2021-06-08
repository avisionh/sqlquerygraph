ARG PY_VER=3.8.0
FROM python:${PY_VER} AS sqlqeurygraph-py

# build requirements
COPY ./neo4j ./

## Add the wait script to the image
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait

RUN mkdir /app \
        && mkdir /import \
        && mkdir /data \
        && pip install py2neo \
        && chmod +x /wait

COPY neo4j/*csv import/
COPY neo4j/*cypher data/
COPY ./loader.py .

CMD /wait
