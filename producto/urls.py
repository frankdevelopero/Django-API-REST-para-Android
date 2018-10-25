from django.urls import path
from producto.ProductoViewset import ProductoViewSets
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('producto', ProductoViewSets, base_name='producto')

urlpatterns = [

]

urlpatterns += router.urls