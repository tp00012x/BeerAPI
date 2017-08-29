from rest_framework import serializers
from .models import BeerModel, RateModel

class BeerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerModel
        fields = '__all__'

class RateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateModel
        fields = '__all__'