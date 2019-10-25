=====
log
=====

log is a simple Django app to allow user registration and login. For each
dashboard users will be able to leave a feedback inform of a contact page.



Quick start
-----------

1. Add "log" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'log',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'', include('log.urls')),

3. Run `python manage.py migrate` to create the log models.

4. Start the development server and visit http://127.0.0.1:8000/login/
   

5. Visit http://127.0.0.1:8000/register/ to create your account which will then allow you lo login.