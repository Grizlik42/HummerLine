web: gunicorn core.wsgi:application --log-file - --timeout 120 --workers 2 --worker-class sync --max-requests 1000 --max-requests-jitter 50
