web: gunicorn send_mail.wsgi
web: python manage.py collectstatic --no-input; gunicorn send_mail.wsgi --log-file - --log-level debug