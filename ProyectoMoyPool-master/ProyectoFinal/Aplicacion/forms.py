from django import forms

class Formulario_Registro_Cliente(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Nombre',
        'data-sb-validations': 'required'
    }))
    apellido = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Apellido',
        'data-sb-validations': 'required'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Email Address',
        'data-sb-validations': 'required,email'
    }))
    
class Formulario_Busqueda_Cliente(forms.Form):
    email = forms.EmailField(label='Email del Cliente', required=True)