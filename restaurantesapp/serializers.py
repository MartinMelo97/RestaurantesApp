from rest_framework import serializers
from .models import RestaurantModel
from django.contrib.auth.models import User
from platillos.models import Platillo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PlatilloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platillo
        fields = ['nombre']


class RestaurantSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)
    platillos = PlatilloSerializer(many=True, read_only=True)

    class Meta:
        model = RestaurantModel
        fields = '__all__'