#!/bin/bash

# Update system packages
sudo apt update
sudo apt upgrade -y

# Install required packages
sudo apt install -y python3-pip python3-venv nginx

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Clone the repository (replace with your repository URL)
# git clone <your-repo-url>
# cd flask-todo

# Install dependencies
poetry install

# Setup Nginx
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

# Enable the Nginx site
sudo ln -s /etc/nginx/sites-available/flask-todo /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl restart nginx

# Create systemd service
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

# Start and enable the service
sudo systemctl start flask-todo
sudo systemctl enable flask-todo 