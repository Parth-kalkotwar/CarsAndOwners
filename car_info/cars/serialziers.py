from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cars,Manufacturer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ("id", "name", "cars")
        extra_kwargs = {'cars': {'required': False}}


class CarsSerializers(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(many=True, read_only=True)
    user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Cars
        fields = ('id', 'name', 'model', 'top_speed', 'manufacturer', 'user')
        extra_kwargs = {'manufacturer': {'required': False}}






