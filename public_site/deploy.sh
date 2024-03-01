#!/bin/bash

echo "Starting deployment process..."

# Navigate to the Django project directory
echo "Navigating to the Django project directory..."
cd /var/www/bookscot/public_site/

# Activate the Conda environment
echo "Activating Conda environment..."
source /home/bookofscotland/miniconda3/etc/profile.d/conda.sh
conda activate BOS

# Pull the latest changes from Git
echo "Pulling latest changes from Git repository..."
git pull origin main

# Install any new dependencies from requirements.txt
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Restart the Uvicorn service
echo "Restarting Uvicorn service..."
sudo systemctl restart aibos_uvicorn.service

# Optional: Restart Nginx if it's used as a reverse proxy or for serving static files
echo "Restarting Nginx..."
sudo systemctl restart nginx

echo "Deployment process completed successfully."
