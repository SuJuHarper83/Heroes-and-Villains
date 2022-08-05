from rest_framework import serializers
from .models import SuperType

class SupersTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['id', 'super_type']
