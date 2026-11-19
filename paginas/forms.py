from django import forms
from .models import projeto
from .models import Categoria

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = projeto
        fields = ["nome", "descricao", "ano", "categoria"]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome"]