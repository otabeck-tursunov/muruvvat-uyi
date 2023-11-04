from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *

class YangilikModelViewSet(ModelViewSet):
    queryset = Yangilik.objects.all()
    serializer_class = YangilikSerializer
