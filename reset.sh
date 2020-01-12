#!/bin/bash
# Reset Models and DB

# 1. Remove DB
rm db.sqlite3

# 2. Remove models
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# 3. Create new models
./manage.py makemigrations article customer rent;

# 4. Apply to DB
./manage.py migrate

# 5. Load data
find -name "*.json" -exec ./manage.py loaddata {} \;
