# DevelopsToday News

## How to run project

1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Commit DB migrations
```bash
python manage.py migrate
```
3. Create superuser to get access to admin site
```bash
python manage.py createsuperuser
```
4. Run the server
```bash
python manage.py runserver
```