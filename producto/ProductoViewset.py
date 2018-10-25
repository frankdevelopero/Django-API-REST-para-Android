from rest_framework import viewsets
from producto.ProductoSerializer import ProductoSerializers
from producto.models import Producto


class ProductoViewSets(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializers
