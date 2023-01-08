# Airports-Finder
Plot airports on a map.

![ezgif com-gif-maker](https://user-images.githubusercontent.com/17769668/211164793-77b653f0-bdd1-44bb-8598-5b66f60c5126.gif)

## Requirements
- Python 3.7
- docker & docker-compose
- node & npm

## Quick Start

```shell
make up
```

## Build from source

### Backend

```shell
cd backend
make install
make up-source
```

### Frontend

```shell
cd frontend
npm install
npm run serve
```

## Deploy on local Kubernetes

1. Spin up the local helm repo and docker registry

```shell
make local-docker-compose-local-repo-and-registry-up
```

2. Build the docker images and push them to the local registry

```shell
