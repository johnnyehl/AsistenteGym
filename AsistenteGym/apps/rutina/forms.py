#encoding:utf-8
from django import forms
from .models import *

class CreateRutinaForm(forms.ModelForm):

	class Meta:
		model = Rutina
		
		widgets = {
			'nombre' : forms.TextInput(attrs = {
				'class' : 'form-control',
				'id' : 'first_name',
				'placeholder' : 'Nombre de rutina'
				}),
			'descripcion' : forms.Textarea(attrs = {
				'class' : 'form-control',
				'id' : 'descripcion',
				'placeholder' : 'Descipción de rutina',
				'rows' : 4
				}),
			

		}

class CreateDiaEntrenamientoForm(forms.ModelForm):

	class Meta:
		model = DiaEntrenamiento
		widgets = {
			'rutina' : forms.TextInput(attrs = {
				'class' : 'form-control',
				'id' : 'first_name',
				}),
		}

class DiaEntrenamientoForm(forms.ModelForm):
	'''
	dia = forms.ComboField(widget = forms.TextInput(attrs={
						'class' : 'form-control',
						'placeholder' : 'título'
		}))'''
	class Meta:
		model = DiaEntrenamiento
		exclude = ("rutina",)
	
	def __init__(self, *args, **kwargs):
		super(DiaEntrenamientoForm, self).__init__(*args, **kwargs)
		self.fields['dia'].widget.attrs.update({'class' : 'form-control'})

	#Validamos que el autor no sea menor a 3 caracteres
	def clean_dia(self, *args, **kwargs):
		diccionario_limpio = self.cleaned_data
		dia = diccionario_limpio.get('dia')

		dia_consulta = DiaEntrenamiento.objects.filter(rutina=1)

		for dias in dia_consulta:
			print dias.dia
			print dia
			if dias.dia == dia:
				raise forms.ValidationError("El dia seleccionado ya existe") ##NO IMPRIME!!! FALTA

		#if len(username) < 3:
		#	raise forms.ValidationError("Nombre de usuario debe de contener mas de tres caracteres")

		return dia