# Modern Flask Todo App

A modern, responsive Todo List application built with Flask, SQLite, and Poetry.

## Architecture Diagrams

### Component Diagram
![Component Diagram](https://www.plantuml.com/plantuml/png/RP71IiD048RlUOgX9pq5fQIYKb0GX4t1A2KNJRIJsl4nTsqFVRztUCYAIJ_dlFUUyPttt-yy-MRm0eAYGg9Kc0dG9kWVr2_u1NAqXP4axN0ZA5Kh6rYGpOIYWrJQ2cpI0o4Ik9_u0xy1KXmSKR9MSjYOtE5QWvhWAhG9rrGVJP2-VQVm_FRlTFVR_FBl-FRdEFduE7kA1Zq1)

### Deployment Diagram
![Deployment Diagram](https://www.plantuml.com/plantuml/png/TP11IWD148RlUOgXBpq5fQQYqX0mX4t1A2KNJRIJsl4nTsqFVRztUCYAIJ_dlFUUyPttt-yy-MRm0eAYGg9Kc0dG9kWVr2_u1NAqXP4axN0ZA5Kh6rYGpOIYWrJQ2cpI0o4Ik9_u0xy1KXmSKR9MSjYOtE5QWvhWAhG9rrGVJP2-VQVm_FRlTFVR_FBl-FRdEFduE7kA1Zq1)

### Sequence Diagram
![Sequence Diagram](https://www.plantuml.com/plantuml/png/PP71IWD148RlUOgX9pq5fQQYqX0mX4t1A2KNJRIJsl4nTsqFVRztUCYAIJ_dlFUUyPttt-yy-MRm0eAYGg9Kc0dG9kWVr2_u1NAqXP4axN0ZA5Kh6rYGpOIYWrJQ2cpI0o4Ik9_u0xy1KXmSKR9MSjYOtE5QWvhWAhG9rrGVJP2-VQVm_FRlTFVR_FBl-FRdEFduE7kA1Zq1)

### State Diagram
![State Diagram](https://www.plantuml.com/plantuml/png/PP71IWD148RlUOgX9pq5fQQYqX0mX4t1A2KNJRIJsl4nTsqFVRztUCYAIJ_dlFUUyPttt-yy-MRm0eAYGg9Kc0dG9kWVr2_u1NAqXP4axN0ZA5Kh6rYGpOIYWrJQ2cpI0o4Ik9_u0xy1KXmSKR9MSjYOtE5QWvhWAhG9rrGVJP2-VQVm_FRlTFVR_FBl-FRdEFduE7kA1Zq1)

### Deployment Flow
![Deployment Flow](https://www.plantuml.com/plantuml/png/PP71IWD148RlUOgX9pq5fQQYqX0mX4t1A2KNJRIJsl4nTsqFVRztUCYAIJ_dlFUUyPttt-yy-MRm0eAYGg9Kc0dG9kWVr2_u1NAqXP4axN0ZA5Kh6rYGpOIYWrJQ2cpI0o4Ik9_u0xy1KXmSKR9MSjYOtE5QWvhWAhG9rrGVJP2-VQVm_FRlTFVR_FBl-FRdEFduE7kA1Zq1)

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
