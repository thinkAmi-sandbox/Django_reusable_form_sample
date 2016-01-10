=====
thinkami_reusable_form_sample
=====

reusable form sample.

Quick start
-----------

1. Run `pip install git+https://github.com/thinkAmi-sandbox/Django_reusable_form_sample.git` to install in your project.

2. Add "thinkami_reusable_app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'thinkami_reusable_app',
    ]

3. Include the thinkami_reusable_app URLconf in your project urls.py like this::

    url(r'^reuse/', include('thinkami_reusable_app.urls', namespace='myform')),

4. Run `python manage.py migrate` to create the app models.

5. Run `python manage.py loaddata initial_data` for thinkami_reusable_app's initial data.

6. Start the development server.

7. Visit http://127.0.0.1:8000/reuse/register to participate in the app.
