from rest_framework import serializers
from .models import Baston

class BastonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Baston
		fields = ["fecha","comentario"]

class BastonSerializerV2(serializers.ModelSerializer):
  class Meta:
    model = Baston
    exclude = []