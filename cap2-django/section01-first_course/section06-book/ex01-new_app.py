"""
    In this section, we'll explore more of django with a book titled:
        
        Art Yudin - Building Versatile Mobile Apps with Python and RESTful Web Services 
        with Django and React (2020)

"""

"""
    First, we'll create a new app for our project.
        python manage.py startapp stores
"""

# And add it to settings.py INSTALLED_APPS array:        
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'app',
    'stores'
]
