# Flask Todo Application with AWS Deployment - Generation Prompt

This document contains the complete prompt to generate and deploy a modern Flask Todo application with AWS infrastructure.

## Application Requirements

### 1. Backend
- Flask web framework
- SQLite database using SQLAlchemy
- RESTful routes for CRUD operations
- Poetry for dependency management
- Gunicorn for production server

### 2. Frontend
- Modern, responsive design
- Clean UI with CSS variables
- Support for adding, completing, and deleting todos
- Optional descriptions for todos
- Timestamp tracking
- Google Fonts (Inter) for typography

### 3. Infrastructure (AWS CDK)
- Single EC2 instance (t2.micro) deployment
- VPC with public subnet only (no NAT Gateway needed)
- Security group for HTTP and SSH access
- Nginx as reverse proxy
- Systemd service for automatic startup
- Proper SSH key handling for secure access

### 4. Project Structure
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
├── deploy/
│   └── setup.sh
├── infrastructure/
│   ├── app.py
│   ├── cdk.json
│   └── requirements.txt
├── .gitignore
├── gunicorn_config.py
├── pyproject.toml
└── README.md
```

### 5. Deployment Requirements
- Automated setup script
- Non-interactive installation
- Proper error handling
- Clear logging of setup steps
- Systemd service configuration
- Nginx configuration
- Poetry virtual environment setup

### 6. Security Considerations
- SSH key-based access only
- Proper file permissions
- Security group restrictions
- No hardcoded secrets

### 7. Development Setup
- Poetry for dependency management
- Local development configuration
- Git repository setup with proper .gitignore
- Documentation for local development

### 8. Production Setup
- Gunicorn with multiple workers
- Nginx reverse proxy
- Systemd service for automatic restarts
- Log rotation
- Error handling and reporting

## Deployment Instructions

The application should be deployable with a single command after initial AWS configuration:

1. Configure AWS credentials
2. Generate SSH key pair
3. Deploy infrastructure with CDK
4. Application automatically deploys via user-data script

The deployment process should be idempotent (can be run multiple times without issues).

## Key Features to Implement

### Todo Items
- Title (required)
- Description (optional)
- Completion status
- Creation timestamp
- Ability to mark as complete/incomplete
- Ability to delete

### User Interface
- Clean, modern design
- Responsive layout
- Smooth animations
- Clear feedback on actions
- Empty state handling
- Loading states

### Infrastructure
- Automatic SSL/TLS setup (optional)
- Automatic backups (optional)
- Health checks
- Error logging
- Performance monitoring

## Development Workflow

1. Local development with Poetry
2. Testing with pytest
3. Git workflow with proper branching
4. AWS CDK for infrastructure as code
5. Automated deployment process

## Notes

This prompt is designed to generate a production-ready Flask application with modern development practices and robust deployment procedures. The focus is on maintainability, security, and user experience. 