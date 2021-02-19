"""
    https://stackoverflow.com/questions/35760943/how-can-i-enable-cors-on-django-rest-framework

    (env) pip3 install django-cors-headers

    pip freeze > requirements.txt
"""


# On settings.py, add it to installed apps

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'posts',
    'postsgenerics',
    'corsheaders',
]


# Add it to middleware

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # here
    'django.middleware.common.CommonMiddleware', # and here
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

"""
    NOTE: The documentation says "CorsMiddleware should be placed as high as possible, 
    especially before any middleware that can generate responses such as Django's 
    CommonMiddleware or Whitenoise's WhiteNoiseMiddleware"
"""


# Still in settings.py, you can add the CORS configurations:

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000', # Client URL
]
CORS_ORIGIN_REGEX_WHITELIST = [
    'http://localhost:3000',
]

# NOTE: To allow access from all origins => CORS_ORIGIN_ALLOW_ALL = True


"""
    Cors headers documentation:
        https://github.com/adamchainz/django-cors-headers

    Test:
    
    To test cors, create an express project serving an html page on the port 3001, it should
    block request.

    Then change the port to 3000, and the requests should succeed
"""
