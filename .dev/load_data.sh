#!/bin/sh

# Load (seed the database) with some critical data to our app
python3 manage.py loaddata zaid/seed/001_Status.json