#!/bin/bash

set -e

if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
else
    echo "Creating and activating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
fi

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Installing Node.js dependencies..."
npm install

echo "Running Django migrations..."
python manage.py migrate

echo "Creating default users..."
python manage.py create_default_users

echo "Starting Django development server..."
python manage.py runserver
