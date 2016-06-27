from django.conf.urls import url
from .views import Mes, Esta, Actualizar, Estaciones, Puno, Excel
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mes/', Mes.as_view(), name='mes'),
    url(r'^estaciones/', Esta.as_view(), name='estaciones'),
    url(r'^entrada/', Actualizar.as_view(), name='entrada'),
    url(r'^estacion/(?P<pk>\d+)/', Estaciones.as_view(), name='estaciones'),
    url(r'^estacioneso/(?P<pk>\d+)/', 'temp.views.estacionver', name='ees'),
    url(r'^esta/(?P<pk>\d+)/', Puno.as_view(), name='puno'),
    url(r'^prueba/(?P<pk>\d+)/', 'temp.views.prueba', name='prueba'),
    #va para actualizar
    url(r'^excel/(?P<pk>\d+)/', Excel.as_view(), name='miexcel'),
]