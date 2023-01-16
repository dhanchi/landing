build:
    docker:
        web: Dockerfile
release:
    image: web
    command:
        - python manage.py collectstatic --noinput
run:
    web: gunicorn home.wsgi