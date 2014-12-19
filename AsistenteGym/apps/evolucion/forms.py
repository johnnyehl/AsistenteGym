#encoding: utf-8
from django import forms
from .models import Evolucion

class evolucionForm(forms.ModelForm):

	class Meta:
		model = Evolucion
		exclude = ()
		widgets = {
			
			'peso' : forms.TextInput(attrs = {
				'min':"30",
				'max':"200",
				'required':'Tre',
				'type' : 'number',
				 'step': '0.01',
				'class' : 'form-control',
				'id' : 'peso',
				'placeholder' : 'Peso corporal en kg',
				'onkeyup':'if(validarEnter(event)== true){location.reload();}',
				}),
			'hombro' : forms.TextInput(attrs = {
				'min':"35",
				'max':"150",
				'required':'Tre',
				'type' : 'number',
				#'step': '0.01',
				'class' : 'form-control',
				'id' : 'hombro',
				'placeholder' : 'Medida de hombro',
				'onkeyup':'if(validarEnter(event)== true){location.reload();}',
				}),
			'pecho' : forms.TextInput(attrs = {
				'min':"35",
				'max':"150",
				'required':'Tre',
				'type' : 'number',
				'step': '0.01',
				'class' : 'form-control',
				'id' : 'hombro',
				'placeholder' : 'Medida de Pecho',
				'onkeyup':'if(validarEnter(event)== true){location.reload();}',
				}),
			'cintura' : forms.TextInput(attrs = {
				'min':"30",
				'max':"200",
				'required':'Tre',
				'type' : 'number',
				'class' : 'form-control',
				'id' : 'cintura',
				'placeholder' : 'Medida de Cintura',
				'onkeyup':'if(validarEnter(event)== true){location.reload();}',
				}),
			'brazo' : forms.TextInput(attrs = {
				'min':"10",
				'max':"80",
				'required':'Tre',
				'type' : 'number',
				'class' : 'form-control',
				'id' : 'brazo',
				'placeholder' : 'Medida de brazo',
				'onkeyup':'if(validarEnter(event)== true){location.reload();}',
				}),
			'antebrazo' : forms.TextInput(attrs = {
				'min':"10",
				'max':"40",
				'required':'Tre',
				'type' : 'number',
				'class' : 'form-control',
				'id' : 'antebrazo',
				'placeholder' : 'Medida de antebrazo',
				'onkeyup':'if(validarEnter(event)== true){location.reload();}',
				}),
			'pierna' : forms.TextInput(attrs = {
				'min':"25",
				'max':"90",
				'type' : 'number',
				'class' : 'form-control',
				'id' : 'pierna',
				'placeholder' : 'Medida de pierna',
				'onkeyup':'if(validarEnter(event)== true){location.reload();}',
				'required':'Tre',
				}),
			'pantorrillas' : forms.TextInput(attrs = {
				'min':"10",
				'max':"40",
				'required':'Tre',
				'type' : 'number',
				'class' : 'form-control',
				'id' : 'pantorrillas',
				'placeholder' : 'Medida de pantorrilla',
				'onkeyup':'if(validarEnter(event)== true){location.reload();}',
				}),
			'gluteos' : forms.TextInput(attrs = {
				'min':"40",
				'max':"150",
				'required':'Tre',
				'type' : 'number',
				'class' : 'form-control',
				'id' : 'gluteos',
				'placeholder' : 'Medida de gluteo',
				'onkeyup':'if(validarEnter(event)== true){location.reload();}',
				}),
			
			

		}

	