from django import forms
from .models import Alumno
from .models import Materia

class FormularioAlumno(forms.ModelForm):
	class Meta:
		model = Alumno
		fields=["nombres","apellidos","cedula","correo","celular"]

class FormularioAlumnoModificar(forms.ModelForm):
	class Meta:
		model = Alumno
		fields=["nombres","apellidos","correo","celular"]
			
class FormularioMateria(forms.ModelForm):
	class Meta:
		model = Materia
		fields=["nombre","cupos","descripcion"]
		
class FormularioMateriaModificar(forms.ModelForm):
	class Meta:
		model = Materia
		fields=["nombre","cupos","descripcion"]


