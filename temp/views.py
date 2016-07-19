from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import TermoPlu, Estacion

class Mes(ListView):
	template_name = 'temp/index1.html'
	model = TermoPlu

class Esta(ListView):
	template_name = 'temp/estaciones.html'
	model = Estacion

class Actualizar(ListView):
	template_name = 'temp/index.html'
	model = TermoPlu
	ordering = 'estacion'

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

class Estaciones(TemplateView):
	template_name = 'temp/estacion.html'
	model = TermoPlu

#valeeeee para intranet <-----
def estacionver(request, pk):
	estacion = TermoPlu.objects.filter(estacion=pk)
	return render(request, 'temp/estacion.html', {'dato': estacion})

#para puno
class Puno(DetailView):
	template_name = 'temp/esta.html'
	model = Estacion
	slug_field = 'codpuno'
	context_object_name = 'estaes'
	def get_context_data(self, **kwargs):
		context = super(Puno, self).get_context_data(**kwargs)
		valor = Estacion.objects.get(codpuno = self.kwargs['pk'])
		context['estaenpuno'] = valor
		context['temp'] = TermoPlu.objects.filter(estacion = valor)
		context['numero'] = (int(valor.codpuno) - 1 ) * 31
		return context
	
def prueba(request, pk):
	estacion = TermoPlu.objects.filter(estacion=pk)
	return render(request, 'temp/prueba.html', {'dato': estacion})

#para sacar mensuales
class Excel(DetailView):
	template_name = 'temp/excel.html'
	model = Estacion
	slug_field = 'id'
	context_object_name = 'estaes'
	def get_context_data(self, **kwargs):
		context = super(Excel, self).get_context_data(**kwargs)
		valor = Estacion.objects.get(id = self.kwargs['pk'])
		context['miestacion'] = valor #tratar de eliminar
		context['mes1'] = TermoPlu.objects.filter(estacion = valor, fecha__month=1)
		context['mes2'] = TermoPlu.objects.filter(estacion = valor, fecha__month=2)
		context['mes3'] = TermoPlu.objects.filter(estacion = valor, fecha__month=3)
		context['mes4'] = TermoPlu.objects.filter(estacion = valor, fecha__month=4)
		context['mes5'] = TermoPlu.objects.filter(estacion = valor, fecha__month=5)
		context['mes6'] = TermoPlu.objects.filter(estacion = valor, fecha__month=6)
		return context