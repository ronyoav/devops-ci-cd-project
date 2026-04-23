#!/bin/bash

echo "Starting app..."
python app.py &

sleep 5

echo "Checking health..."
python check_app.py