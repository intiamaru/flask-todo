# Simple Flask Todo App with AWS Deployment

Create a basic todo list application using Flask and deploy it to AWS using CDK.

## Application Features

### Backend
- Flask application with SQLite database
- Basic CRUD operations for todos
- Poetry for Python dependency management

### Frontend
- Simple, clean interface
- Add todos with optional descriptions
- Mark todos as complete/incomplete
- Delete todos
- Show creation timestamps

### AWS Infrastructure
- Single EC2 instance (t2.micro)
- Basic VPC with public subnet
- Security group for HTTP and SSH
- Nginx as reverse proxy
- Automatic deployment via setup script

## Project Structure
```
flask-todo/
├── app/                      # Flask application
│   ├── __init__.py          # App initialization
│   ├── models.py            # Todo model
│   ├── routes.py            # API routes
│   ├── static/css/          # Styling
│   └── templates/           # HTML templates
├── deploy/
│   └── setup.sh            # Server setup script
├── infrastructure/          # AWS CDK code
├── gunicorn_config.py      # Gunicorn settings
└── pyproject.toml          # Poetry dependencies
```

## Deployment Steps

1. Set up AWS credentials locally
2. Create SSH key pair for EC2 access
3. Deploy with CDK
4. Access application via EC2 public IP

## Required Tools

- Python 3.9+
- Poetry
- AWS CLI
- AWS CDK
- Git

## Development Instructions

1. Clone repository
2. Install dependencies with Poetry
3. Run Flask locally for development
4. Deploy to AWS using CDK

That's it! A simple todo application that can be deployed to AWS with minimal configuration. 