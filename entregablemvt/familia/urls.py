from django.urls import path
from familia import views

urlpatterns = [
    path('', views.inicio2, name='inicio2'),
    path('verfamilia/', views.verfamilia, name='verfamilia'),
    path('vermascota/', views.vermascota, name='vermascota'),
    path('cargarpersona/', views.cargar_persona, name='cargar_persona'),
    path('cargarmascota/', views.cargar_mascota, name='cargar_mascota'),
    path('buscarpersona/', views.buscar_persona, name='buscar_persona'),
    path('buscarmascota/', views.buscar_mascota, name='buscar_mascota'),
]