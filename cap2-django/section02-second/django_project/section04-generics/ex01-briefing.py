"""
In this section, we'll create a new app, import the models and serializers from the previous app, 
but write generic API views instead of viewsets.

python manage.py startapp postsgenerics

Note: Don't forget to add the app to INSTALLED_APPS
"""


"""
Then, we'll create the local urls.py file and we'll import it on the global urls.py
"""

# postsgenerics urls.py
from django.urls import path, include

urlpatterns = [
    
]

# project urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('posts.urls')),
    path('generics/', include('postsgenerics.urls'))
]

