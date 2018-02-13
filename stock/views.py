from django.shortcuts import render

# Conjunto de vistas, el del listado y el del objeto como tal.
from rest_framework import viewsets

from models import Producto
from .serializers import PROSerializer

class PROViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = PROSerializer
