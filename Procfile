release: -sh c "python manage.py migrate && python manage.py collectstatic --noinput"

web: gunicorn splita.wsgi