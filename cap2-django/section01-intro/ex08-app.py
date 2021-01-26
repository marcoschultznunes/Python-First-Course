"""
We can use the command
    python manage.py startapp app

to initialize an app folder containing the following files:
    migrations (folder)
    admin.py,
    apps.py, => Will not be modified
    models.py,
    tests.py,
    views.py
"""


"""
    Then on settings.py we'll add the app to the INSTALLED_APPS list:
"""

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
]

