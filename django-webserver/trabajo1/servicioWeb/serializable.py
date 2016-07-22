


#tranformar los objetos y dar propiedad para que se puedan

from rest_framework import serializers  
from administrador.models import Materia
from administrador.models import Alumno  

class  MateriaSerializable(serializers.ModelSerializer): # los parentesis () es para herencia
	class Meta:
		model=Materia
		fields=['idMateria','nombre','cupos','descripcion']

class  AlumnoSerializable(serializers.ModelSerializer): # los parentesis () es para herencia
	class Meta:
		model=Alumno
		fields=['nombres','apellidos','cedula','correo','celular']