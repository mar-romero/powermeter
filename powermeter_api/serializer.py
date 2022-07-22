import re
from attr import dataclass
from rest_framework import serializers
from powermeter_api.models import Mediciones

class MedicionesSerializer(serializers.Serializer):
    mediciones = serializers.FloatField()

    def create(self,data):
        return Mediciones.objects.create(**data)
