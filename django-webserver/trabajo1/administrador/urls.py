from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', 'administrador.views.listar'),
    url(r'^crearAlumno/$', 'administrador.views.crearAlumno'),
    url(r'^crearMateria/$', 'administrador.views.crearMateria'),

    url(r'^modificarAlumno/$', 'administrador.views.modificarAlumno'),
    url(r'^modificarMateria/$', 'administrador.views.modificarMateria'),
    url(r'^eliminarA/$', 'administrador.views.eliminarA'),
    url(r'^eliminarAlumno/$', 'administrador.views.eliminarAlumno'),
    url(r'^eliminarM/$', 'administrador.views.eliminarM'),
    url(r'^eliminarMateria/$', 'administrador.views.eliminarMateria'),
    
]