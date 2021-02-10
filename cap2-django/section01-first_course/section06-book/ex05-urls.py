"""
    API Views cannot be registered to router.py.

    We need to use a local urls.py and add it to the global urls.py
"""

# stores urls.py
from django.urls import path, include
from .views import PizzeriaListAPIView, PizzeriaRetrieveAPIView

urlpatterns = [
    path('pizzerias/', PizzeriaListAPIView.as_view()),
    path('pizzerias/<int:pk>/', PizzeriaRetrieveAPIView.as_view()),
    path('pizzerias/create', PizzeriaCreateAPIView.as_view()),
    path('pizzerias/update/<int:pk>/', PizzeriaRetrieveUpdateAPIView.as_view()),
    path('pizzerias/delete/<int:pk>/', PizzariaRetrieveDestroyAPIView.as_view())
]


# global urls.py
from django.contrib import admin
from django.urls import path, include
from app.router import router as app_router
from app.views import hello 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello),
    path('app/', include(app_router.urls)),
    path('store/', include('stores.urls'))
]
