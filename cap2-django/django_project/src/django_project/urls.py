from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from app.router import router as app_router
from app.views import hello 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
    path('app/', include(app_router.urls)),
    path('store/', include('stores.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
