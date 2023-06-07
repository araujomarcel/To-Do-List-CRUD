from django.contrib import admin
from django.forms import DateTimeField
from .models import AtividadeModel

# Register your models here.

class AtividadeModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'descricao', 'data','modificado_em')
    date_hierarchy = 'modificado_em'
    search_fields = ('nome', 'data')
    list_filter = ('modificado_em',)
def registrado_esse_ano(self, obj):
    hoje = DateTimeField.today()
    return obj.modificado_em.year == hoje.year

    
registrado_esse_ano.short_description = 'Registrado este registrado_esse_ano.boolean = True'

admin.site.register(AtividadeModel, AtividadeModelAdmin)
