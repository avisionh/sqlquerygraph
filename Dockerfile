ARG PY_VER=3.8.0
FROM python:${PY_VER} AS sqlqeurygraph-py

## Add the wait script to the image
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait

# install package for loader and give it executable rights
RUN pip install py2neo \
    && chmod +x /wait

# move relevant files so they can be executed
COPY ./loader.py ./
COPY ./neo4j/*.cypher ./data
