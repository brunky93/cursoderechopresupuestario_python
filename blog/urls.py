from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('material.html', views.material, name='material'),
    path('videos.html', views.videos, name='videos'),
    path('contacto.html', views.contacto, name='contacto'),
    path('libro0.html', views.vinculacion, name='vinculacion'),
    path('libro1.html', views.caja, name='caja'),
    path('libro2.html', views.pagos, name='pagos'),
    path('libro3.html', views.presupuesto, name='presupuesto'),
]
