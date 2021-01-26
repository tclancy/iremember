iremember
=========

Django app for relatives with dementia

Next Steps/ Days
================

- Want to be able to communicate problems, e.g., "The TV isn't working" 
  without having to go up and down stairs and forget why.  
- Figure out JS story
- Replace static calendar icon with dynamic day
- Track down git ignore weirdness


Settings
--------

See [their docs](http://cookiecutter-django.readthedocs.io/en/latest/settings.html) and 
decide if we want to keep these

Basic Commands
--------------

### Type checks

Running type checks with mypy: `mypy iremember`

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

### Running tests with py.test

`pytest`

### Live reloading and Sass CSS compilation

[Their docs](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html)


### Celery

This app comes with Celery.

To run a celery worker: `celery -A config.celery_app worker -l info`

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.
