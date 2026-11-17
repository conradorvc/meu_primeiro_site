from django.contrib import admin

from .models import filme
from .models import Categoria
from .models import projeto

admin.site.register(filme)
admin.site.register(Categoria)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nome', 'descricao')
    
admin.site.register(projeto, ProjetoAdmin)
# Register your models here.
