from django.contrib import admin

# Register your models here.
from .models import Materia

class AdminMateria(admin.ModelAdmin):
	list_display = ["__str__","idMateria","nombre","cupos","descripcion"]
	list_editable = ["idMateria","nombre","cupos","descripcion"]
	list_filter=["nombre"]
	search_fields = ["idMateria","nombre","cupos","descripcion"]

	class Meta:
		model = Materia

admin.site.register(Materia,AdminMateria)
