# On settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', # This is the app that provides the default Django authentication
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'posts',
    'postsgenerics',
    'corsheaders',
]


"""
    To use the auth app we need to add it to our project-level urls.py file. 
    Make sure to add include on the second line.
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # Adds the auth routes.
    path('blog/', include('posts.urls')),
    path('generics/', include('postsgenerics.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



"""
Auth routes (given that the route was named "accounts")

accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']

NOTE: The default Django auth app uses templates, when using REST framework you can use 
django-rest-auth, or create our own views instead of using the default.

django-rest-auth:
    https://django-rest-auth.readthedocs.io/en/latest/installation.html
"""
