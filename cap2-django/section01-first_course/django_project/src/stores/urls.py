from django.urls import path, include
from .views import *

urlpatterns = [
    path('pizzerias/', PizzeriaListAPIView.as_view()),
    path('pizzerias/<int:pk>/', PizzeriaRetrieveAPIView.as_view()),
    path('pizzerias/create', PizzeriaCreateAPIView.as_view()),
    path('pizzerias/update/<int:pk>/', PizzeriaRetrieveUpdateAPIView.as_view()),
    path('pizzerias/delete/<int:pk>/', PizzariaRetrieveDestroyAPIView.as_view())
]
