release: -sh c "python manage.py migrate && python manage.py collectstatic --noinput"
web: -sh c "cd splita && gunicorn splita.wsgi:application"