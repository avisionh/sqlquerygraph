ARG PY_VER=3.8.0
FROM python:${PY_VER} AS sqlqeurygraph-py

## Add the wait script to the image
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait

# download pipenv so can create requirements.txt
# for faster environment recreation
# https://pythonspeed.com/articles/pipenv-docker/
RUN pip install --upgrade pip \
    && pip install poetry
COPY poetry.lock ./tmp
COPY pyproject.toml ./
RUN poetry export -f requirements.txt -o requirements.txt

# move relevant folders and files from local to container
COPY ./example ./example
COPY sqlquerygraph.py ./
COPY exporter.py ./
COPY extractor.py ./
COPY writer.py ./
COPY loader.py ./

# install package for loader and give it executable rights
RUN pip install -r requirements.txt \
    && mkdir log \
    && mkdir data \
    && mkdir neo4j \
    && python sqlquerygraph.py -sd 'example' -ed 'neo4j' -rd 'github_repos' 'analytics' 'reporting'
    && chmod +x /wait

# move relevant files so they can be executed
COPY ./neo4j/*.cypher ./data
