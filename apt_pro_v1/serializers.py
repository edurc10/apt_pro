from rest_framework.serializers import ModelSerializer
from .models import AptdealToday

class TestDataSerializer(ModelSerializer):
    class Meta:
        model = AptdealToday
        fields = '__all__'