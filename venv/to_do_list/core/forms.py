from .models import AtividadeModel
from django.forms import ModelForm

class AtividadeModelForm(ModelForm):
    class Meta:
        model=AtividadeModel
        fields=['nome', 'descricao', 'tipo', 'data']