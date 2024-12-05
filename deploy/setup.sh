#!/bin/bash

# Exit on error
set -e

# Avoid prompts
export DEBIAN_FRONTEND=noninteractive

echo "Starting setup..."

echo "Updating system packages..."
sudo apt-get update
sudo apt-get upgrade -y

echo "Installing required packages..."
sudo apt-get install -y python3-pip python3-venv nginx

echo "Installing Poetry..."
curl -sSL https://install.python-poetry.org | POETRY_HOME=/home/ubuntu/.local python3 -

# Add poetry to PATH for this session
export PATH="/home/ubuntu/.local/bin:$PATH"

echo "Installing project dependencies..."
poetry config virtualenvs.create true
poetry config virtualenvs.in-project true
poetry install --no-interaction

echo "Setting up Nginx..."
sudo tee /etc/nginx/sites-available/flask-todo << EOF
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF

echo "Configuring Nginx..."
sudo ln -sf /etc/nginx/sites-available/flask-todo /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo systemctl restart nginx

echo "Creating systemd service..."
sudo tee /etc/systemd/system/flask-todo.service << EOF
[Unit]
Description=Flask Todo App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/flask-todo
Environment="PATH=/home/ubuntu/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ExecStart=/home/ubuntu/.local/bin/poetry run gunicorn -c gunicorn_config.py 'app:app'
Restart=always

[Install]
WantedBy=multi-user.target
EOF

echo "Starting and enabling service..."
sudo systemctl daemon-reload
sudo systemctl enable flask-todo
sudo systemctl start flask-todo

echo "Setup completed successfully!"
echo "You can check the service status with: sudo systemctl status flask-todo" 