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
4. Install and run Redis server
```bash
redis-server
```
5. Run Celery worker
```bash
celery -A develops_today_news worker --pool=solo -l info 
```
and Celery beat
```bash 
celery -A develops_today_news beat -l info 
```
6. Run the server
```bash
python manage.py runserver
```

Postman https://www.postman.com/collections/bf4855d9ca21a8cf6809