#encoding:utf-8
from django import forms
from .models import User #importamos el modelo User

class ExtraDataForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'dni') #le decimos que solo nos importe el username y el email

	def __init__(self, *args, **kwargs):
		super(ExtraDataForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class' : 'form-control'})

	#Validamos que el autor no sea menor a 3 caracteres
	def clean_username(self):
		diccionario_limpio = self.cleaned_data
		username = diccionario_limpio.get('username')

		if len(username) < 3:
			raise forms.ValidationError("Nombre de usuario debe de contener mas de tres caracteres")

		return username

	def clean_dni(self):
		diccionario_limpio = self.cleaned_data
		dni = diccionario_limpio.get('dni')

		if dni < 1000 and dni >9999:
			raise forms.ValidationError("el DNI debe de tener 8 dígitos")

		return dni


'''
	def clean_first_name(self):
		diccionario_limpio = self.cleaned_data
		first_name = diccionario_limpio.get('first_name')

		if len(first_name) < 3:
			raise forms.ValidationError("El campo nombre debe de contener mas de tres caracteres")

		return first_name

	def clean_last_name(self):
		diccionario_limpio = self.cleaned_data
		last_name = diccionario_limpio.get('last_name')

		if len(last_name) < 3:
			raise forms.ValidationError("El campo apellidos debe de contener mas de tres caracteres")

		return last_name
  '''