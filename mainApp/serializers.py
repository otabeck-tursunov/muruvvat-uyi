from rest_framework.serializers import ModelSerializer
from .models import *

class YangilikSerializer(ModelSerializer):
    class Meta:
        model = Yangilik
        fields = '__all__'