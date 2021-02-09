from rest_framework import serializers
from .models import Pizzeria

class PizzeriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = [
            'id', 'name', 'city', 'zipcode', 'phone', 'email'
        ]

class PizzeriaDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzeria
        fields = '__all__'
