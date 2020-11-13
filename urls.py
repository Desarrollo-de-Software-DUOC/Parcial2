from django.urls import path
from . import views

urlpatterns = [
	path('plantilla', views.plantilla, name='plantilla' ),
	path('registro', views.registro, name='registro'),	
	path('productos', views.productos, name='productos'),	
	path('producto', views.producto, name='producto'),	
	path('sucursal', views.sucursal, name='sucursal'),	
]

# 127.0.0.1:8000/plantilla
# 127.0.0.1:8000/pla
# 127.0.0.1:8000/registro
# 127.0.0.1:8000/sucursal