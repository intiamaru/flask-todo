# Modern Flask Todo App

A modern, responsive Todo List application built with Flask, SQLite, and Poetry.

## Features

- Add, complete, and delete todos
- Optional descriptions for todos
- Modern and responsive design
- SQLite database for persistence
- Poetry for dependency management

## Setup

1. Make sure you have Python 3.9+ and Poetry installed
2. Clone this repository
3. Install dependencies:

```bash
poetry install
```

## Running the Application

1. Activate the virtual environment:

```bash
poetry shell
```

2. Run the Flask application:

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

3. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
flask-todo/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   └── templates/
│       ├── base.html
│       └── index.html
├── poetry.lock
└── pyproject.toml
```
