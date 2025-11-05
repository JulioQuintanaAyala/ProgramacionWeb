# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('noticias/', views.noticias, name='noticias'),
    path('inscripciones/', views.inscripciones, name='inscripciones'),
    path('contacto/', views.contacto, name='contacto'),
    path('oferta/', views.oferta, name='oferta'),
]
