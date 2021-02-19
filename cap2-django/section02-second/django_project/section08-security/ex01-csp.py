"""
    (env) pip3 install django-csp

    pip freeze > requirements.txt
"""

# On settings.py, add it to middleware:

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'csp.middleware.CSPMiddleware', # CSP middleware, right after CORS middleware.
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Add configuration on settings.py:
CSP_DEFAULT_SRC = ("'none'",)
CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')
CSP_SCRIPT_SRC = ("'self' 'unsafe-inline'") # 'unsafe-inline' => Allows inline scripts, don't use it in production
CSP_FONT_SRC = ("'self'", 'fonts.gstatic.com')
CSP_IMG_SRC = ("'self'",)

"""
    NOTE: Google chrome and some other browsers might ignore the 'unsafe-inline' CSP 
    configuration.
"""
