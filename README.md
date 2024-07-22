- **eLearning Platform**: Create an eLearning platform including a CMS
  - Build course models
  - Create and use data fixtures
  - Use model inheritance to create polymorphic Content
  - Create a custom model field to order course contents
  - Implement authentication views
  - Build a content management system using class-based views and mixins
  - Restrict access using groups and permissions
  - Build formsets to manage course contents
  - Create drag-and-drop functionality to reorder content in-place using JavaScript and Django
  - Using generic mixins from [django-braces](https://github.com/brack3t/django-braces)
  - Implement public views and student enrolment views
  - Render different type of contents and use [django-embed-video](https://github.com/jazzband/django-embed-video)
  - Cache content using the cache framework
  - Use the [Memached](https://memcached.org/) and Redis cache backends
  - Monitor Redis using [django-redisboard](https://github.com/ionelmc/django-redisboard)
  - Build an API using [Django REST Framework](https://www.django-rest-framework.org/)
  - Create serializers for models and custom API views
  - Handle API authentication and permissions
  - Build API viewsets and routers
  - Consume your API using Python [requests](https://github.com/psf/requests)
  - Create a real-time chat server using Django [Channels](https://github.com/django/channels)
  - Implement a WebSocket consumer/client using Django and JavaScript
  - Use Redis to set up a channel layer
  - Make your WebSocket fully-asynchronous
  - Implement a chat history by persisting chat messages
  - Create settings for multiple environments
  - Configure a production environment using
    -- [Docker Compose](https://docs.docker.com/compose/) with PostgreSQL, Redis,
    -- [Nginx](https://www.nginx.com/),
    -- [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) and
    -- [Daphne](https://github.com/django/daphne)
  - Serve your project securely through HTTPS
  - Use the Django system check framework
  - Build a custom middleware
  - Create custom management commands

## Start your Tailwind watcher

```bash
    source eduenv/bin/activate
```

````bash
    python manage.py runserver
```

```bash
    ./tailwindcss -i ./static/css/tailwind.css -o ./static/css/style.css --watch
```

```bash
    ./tailwindcss -i ./static/css/tailwind.css -o ./static/css/style.css --minify
```
````
