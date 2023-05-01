from rest_framework import serializers
from .models import doner

class DonerSerializer(serializers.ModelSerializer):
    class Meta:
        model = doner
        fields = '__all__'