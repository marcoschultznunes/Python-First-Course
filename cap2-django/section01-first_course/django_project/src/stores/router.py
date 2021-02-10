from rest_framework import routers
from .views import PizzeriaListAPIView, PizzeriaRetrieveAPIView

router = routers.DefaultRouter()

router.register('pizzerias', PizzeriaListAPIView)
