from io import BytesIO

from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
import time

from .models import Alumno
from .models import Materia

from .forms import FormularioAlumno, FormularioMateria, FormularioMateriaModificar, FormularioAlumnoModificar




#from weasyprint import HTML, CSS



def crearAlumno(request):	
	f = FormularioAlumno(request.POST or None)
	if request.method == 'POST':
		if f.is_valid():
			f_data = f.cleaned_data

			a=Alumno()
			#cl.idCA = CajaAhorros.objects.all()[0]
			a.cedula = f_data.get("cedula")
			a.nombres = f_data.get("nombres")
			a.apellidos = f_data.get("apellidos")
			a.correo = f_data.get("correo")
			a.celular = f_data.get("celular")
			if(a.save()!=True):
				messages.add_message(request, messages.SUCCESS, "Se ha ingresado un alumno", fail_silently=True)
				return redirect(listar)

				
			
	context = {
		'f':f,
	}
	return render(request,"alumno.html",context)
# Create your views here.


def modificarAlumno(request):
	#f = FormularioModificarCliente(request.POST or None)	
	f = FormularioAlumnoModificar(request.POST or None)
	alumno = Alumno.objects.get(cedula=request.GET['cedula'])
	context={
		'alumno':alumno,
		'f':f,
	}
	f.fields['nombres'].initial = alumno.nombres
	f.fields['apellidos'].initial = alumno.apellidos
	f.fields["correo"].initial = alumno.correo
	f.fields["celular"].initial = alumno.celular
	
	if request.method == 'POST':
		if f.is_valid():
			datos = f.cleaned_data
			alumno.nombres = datos.get("nombres")
			alumno.apellidos = datos.get("apellidos")
			alumno.correo = datos.get("correo")
			alumno.celular = datos.get("celular")
			if (alumno.save()):
				messages.add_message(request, messages.ERROR, "No se ha modificado el alumno", fail_silently=True)
			else:	
				messages.add_message(request, messages.SUCCESS, "Se ha modificado el alumno", fail_silently=True)
			return redirect(listar)
	
	return render(request,"modificarAlumno.html",context)


def eliminarA(request):
	alumno = Alumno.objects.get(cedula=request.GET['cedula'])
	context = {
		'alumno':alumno,
	}

	return render(request,"eliminarAlumno.html",context)

def eliminarAlumno(request):
	alumno = Alumno.objects.get(cedula=request.GET['cedula'])
	if alumno.delete():
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado el almno", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "No se ha eliminado el alumno", fail_silently=True)
	return redirect(listar)


def crearMateria(request):	
	f = FormularioMateria(request.POST or None)
	if request.method == 'POST':
		if f.is_valid():
			f_data = f.cleaned_data

			m=Materia()
			
			#cl.idCA = CajaAhorros.objects.all()[0]
			#m.idMateria = f_data.get("idMateria")
			m.nombre = f_data.get("nombre")
			m.cupos = f_data.get("cupos")
			m.descripcion = f_data.get("descripcion")
			aux=time.strftime("%H%M%S%Y%m%d")
			m.idMateria = aux
			if(m.save()!=True):
				messages.add_message(request, messages.SUCCESS, "Se ha ingresado una materia", fail_silently=True)
				return redirect(listar)

				
			
	context = {
		'f':f,
	}
	return render(request,"materia.html",context)

def modificarMateria(request):
	#f = FormularioModificarCliente(request.POST or None)	
	f = FormularioMateriaModificar(request.POST or None)
	materia = Materia.objects.get(idMateria=request.GET['idMateria'])
	context={
		'materia':materia,
		'f':f,
	}
	f.fields['nombre'].initial = materia.nombre
	f.fields['cupos'].initial = materia.cupos
	f.fields["descripcion"].initial = materia.descripcion
	
	if request.method == 'POST':
		if f.is_valid():
			datos = f.cleaned_data
			materia.nombre = datos.get("nombre")
			materia.cupos = datos.get("cupos")
			materia.descripcion = datos.get("descripcion")
			if (materia.save()):
				messages.add_message(request, messages.ERROR, "No se ha modificado la materia", fail_silently=True)
			else:	
				messages.add_message(request, messages.SUCCESS, "Se ha modificado la materia", fail_silently=True)
			return redirect(listar)
	
	return render(request,"modificarMateria.html",context)

def eliminarM(request):
	materia = Materia.objects.get(idMateria=request.GET['idMateria'])
	context = {
		'materia':materia,
	}

	return render(request,"eliminarMateria.html",context)

def eliminarMateria(request):
	materia = Materia.objects.get(idMateria=request.GET['idMateria'])
	if materia.delete():
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado la materia", fail_silently=True)
	else:
		messages.add_message(request, messages.ERROR, "No se ha eliminado la materia", fail_silently=True)
	return redirect(listar)

def listar(request):
	alumno = Alumno.objects.all()
	materia = Materia.objects.all()
	context={
		'alumno':alumno,
		'materia':materia,
	}
	return render(request,"listar.html",context)








