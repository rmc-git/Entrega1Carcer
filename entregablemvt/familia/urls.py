from django.urls import path
from familia import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('verfamilia/', views.verfamilia, name='verfamilia'),
    path('vermascota/', views.vermascota, name='vermascota'),
    path('cargarpersona/', views.cargar_persona, name='cargar_persona'),

]