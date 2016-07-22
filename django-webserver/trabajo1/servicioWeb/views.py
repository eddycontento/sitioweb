from administrador.models import Materia
from administrador.models import Alumno 
from rest_framework import viewsets 
from .serializable import MateriaSerializable
from .serializable import AlumnoSerializable

class  MateriaViewSet(viewsets.ModelViewSet):
	#LLamo al objeto serializable
	serializer_class=MateriaSerializable
	##defino la consulta de datos q se enviaran en el views 
	
	#queryset = Materia.objects.filter(cupo__gt=0)
	queryset = Materia.objects.filter(cupos__gt=0, cupos__lte=30)


class  AlumnoViewSet(viewsets.ModelViewSet):
	#LLamo al objeto serializable
	serializer_class=AlumnoSerializable
	queryset=Alumno.objects.all()
	##defino la consulta de datos q se enviaran en el views 
	#queryset=Alumno.objects.all().order_by('nombres')
	

