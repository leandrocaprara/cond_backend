from rest_framework import serializers
from .models import *

class CondominiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominium
        fields = "__all__"