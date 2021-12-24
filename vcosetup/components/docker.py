from pathlib import Path

DOCKERFILE = """FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml /app
COPY poetry.lock /app

RUN poetry install

COPY . /app

CMD ["poetry", "run", "task", "start"]
"""

DOCKERIGNORE = """.env
pg_data/
"""

COMPOSE_API = """version: "3"

services:
  api:
    build: .
    restart: always
    ports:
      - 8080:8080
    env_file: .env
"""

COMPOSE_BOT = """version: "3"

services:
  bot:
    build: .
    restart: always
    env_file: .env
"""

def run(path: Path, svc: str) -> None:
    (path / "Dockerfile").write_text(DOCKERFILE)
    (path / ".dockerignore").write_text(DOCKERIGNORE)
    (path / "docker-compose.yml").write_text(COMPOSE_BOT if svc == "bot" else COMPOSE_API)
