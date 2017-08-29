from rest_framework import serializers
from .models import BeerModel

class BeerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerModel
        fields = '__all__'