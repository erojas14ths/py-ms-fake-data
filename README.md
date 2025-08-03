# Hands-on Fake-Data

It is a project to obtain fake data through REST.<br>
**The objective is to facilitate obtaining fake data for your developments..**

## Contenido

- [Hands-on Fake-Data](#hands-on-smp-template)
    - [Getting started 🚀](#getting-started-)
        - [Prerequisites](#prerequisites)
        - [Deployment 🛠](#deployment-)
    - [Docs 📄](#docs-)
    - [Running the tests 🧪](#running-the-tests-)

## Getting started 🚀

These instructions will allow you to install, deploy and run the project.<br>

### Prerequisites

Install the following requirements:

1. **Install Python**:
    - You can download it from [Python 3](https://www.python.org/downloads/).
    - Verify the installation by running `python --version` at the terminal.
2. **Activar the environment**:
    - Activate the environment `source .venv/bin/activate` at the terminal.
    - Verify the installation by running `which python` at the terminal.
    - Your project route must appear `../smp-template/.venv/bin/python`.
3. **Install the module uvicorn**:
    - Verify the installation by running `pip install uvicorn` at the terminal.
    - For Windows use `python -m pip install uvicorn` at the terminal.
4. **Install the module fastapi**:
    - Verify the installation by running `pip install fastapi` at the terminal.
    - For Windows use `python -m pip install fastapi` at the terminal.
5. **Install the module httpx**:
    - Verify the installation by running `pip install httpx` at the terminal.
    - For Windows use `python -m pip install httpx` at the terminal.
6. **Install the module Faker**:
    - Verify the installation by running `pip install Faker` at the terminal.
    - For Windows use `python -m pip install Faker` at the terminal.

### Deployment 🛠

Follow these steps to run the project on your machine:

1. Go to the root of the repository:

2. Run the main application:

```bash
python main.py
```

## Docs 📄

- Swagger: http://localhost:8080/docs

## Running the tests 🧪

To run automated tests, make sure your development environment is configured correctly and use the following command:

### Package

I. Run package test

```bash
pytest
```
### cURL

I. Person:

```bash
curl -s 'localhost:8080/person' | jq
```

II. Persons:

```bash
curl -s 'localhost:8080/persons?size=1000&unique=true' | jq length
```