from django.utils.text import slugify
from django.db import models


class Alumno(models.Model):
	#student_type = models.CharField(max_length=1, choices=STUDENT_TYPE_CHOICES)
	#idCA = models.ForeignKey(CajaAhorros, on_delete=models.CASCADE,default="")
	nombres = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	cedula = models.CharField(max_length=10,unique=True)
	correo = models.EmailField(max_length=30,blank=True,null=True)
	celular = models.CharField(max_length=15,blank=True,null=True)
	

	def __str__(self):
		return self.cedula
		
	def save(self, *args, **kwargs):
		self.slug = slugify(self.cedula)
		return super().save(*args, **kwargs)


class Materia(models.Model):
	#student_type = models.CharField(max_length=1, choices=STUDENT_TYPE_CHOICES)
	#idCA = models.ForeignKey(Alumno, on_delete=models.CASCADE,default="")
	idMateria = models.IntegerField()
	nombre = models.CharField(max_length=30)
	cupos = models.CharField(max_length=30)
	descripcion = models.TextField(max_length=50,default="descripcion")
	

	def __str__(self):
		return str(self.idMateria)
		
	
