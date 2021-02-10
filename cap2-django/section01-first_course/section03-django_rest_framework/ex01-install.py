# To install django rest framework, we activate the env:
#     source env/bin/activate

# Then we install the DRF to the env using pip:
#     pip3 install djangorestframework


# We also need to add 'rest_framework' to INSTALLED_APPS on settings.py:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'app'
]

# And also add this to settings.py:
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

"""
    There is also an issue with vscode, we need to set the python path to the env python file.
    So in vscode/settings.json:

    {
        "python.pythonPath": "django_project/env/bin/python3.8"
    }
"""
