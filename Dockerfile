ARG PY_VER=3.8.0
FROM python:${PY_VER} AS sqlqeurygraph-py

RUN mkdir /app \
        && mkdir /import \
        && mkdir /data \
        && pip install py2neo

# build requirements
COPY ./loader.py .
COPY data/*csv import/

CMD ["loader.py", "data/query_constraints.cypher"]
ENTRYPOINT ["python3"]
