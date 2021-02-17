"""
    To serve static files in django, we add the following to the project's urls.py:
"""

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('posts.urls')),
    path('generics/', include('postsgenerics.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # This line
