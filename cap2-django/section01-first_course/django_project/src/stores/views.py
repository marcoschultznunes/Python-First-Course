from django.shortcuts import render
from rest_framework import generics
from .serializers import PizzeriaListSerializer, PizzeriaDetailsSerializer
from .models import Pizzeria

class PizzeriaListAPIView(generics.ListAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaListSerializer


class PizzeriaRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailsSerializer

class PizzeriaCreateAPIView(generics.CreateAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailsSerializer

class PizzeriaRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailsSerializer

class PizzariaRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):  
    lookup_field = 'pk'
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailsSerializer
