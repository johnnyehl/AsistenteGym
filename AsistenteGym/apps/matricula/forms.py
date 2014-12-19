#encoding: utf-8
from django import forms
from .models import Matricula

class MatriculaForm(forms.ModelForm):

	class Meta:
		model = Matricula
		
