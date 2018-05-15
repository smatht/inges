from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CompraSerializer
from .models import Compra

class ComprasViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

# Create your views here.
