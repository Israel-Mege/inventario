from django.urls import path, include
from rest_framework import routers
from api import views

routers = routers.DefaultRouter()
routers.register(r'categorias', views.CategoriaViewSet)
routers.register(r'productos', views.ProductoViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
