from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import TermoPlu, Estacion

class TermoResource(resources.ModelResource):
	class Meta:
		model = TermoPlu

class EstaResource(resources.ModelResource):
	class Meta:
		model = Estacion

class TempAdmin(ImportExportModelAdmin):
    resource_class = TermoResource
    pass

#Para Importar
class EstaAdmin(ImportExportModelAdmin):
    resource_class = EstaResource
    pass

class DatAdmin(admin.ModelAdmin):
	list_display = ('estacion','maxi','mini','prec',)
	list_editable = ('maxi','mini','prec',)

#Para Editar
class EstaeAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','codigo','codpuno')
	list_editable = ('codigo','codpuno')

admin.site.register(TermoPlu,TempAdmin)
admin.site.register(Estacion,EstaeAdmin)