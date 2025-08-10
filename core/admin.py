from django.contrib import admin
from .models import Votacao, Escuderia, Criterio, Voto, Nota

# 1. Criada uma classe para personalizar a área de administração do modelo 'Votacao'
class VotacaoAdmin(admin.ModelAdmin):
    # Estes campos aparecerão como colunas na lista de votações, facilitando a visualização.
    list_display = ('nome', 'esta_ativa', 'data_inicio')
    
    # Esta é a configuração mais importante: ela transforma a seleção de critérios
    # em uma caixa dupla (disponíveis / escolhidos), o que é muito mais fácil de usar.
    filter_horizontal = ('criterios',)

# 2. Registramos os outros modelos da forma padrão
admin.site.register(Escuderia)
admin.site.register(Criterio)
admin.site.register(Voto)
admin.site.register(Nota)

# 3. Finalmente, registramos o modelo 'Votacao' usando a classe de configuração personalizada
admin.site.register(Votacao, VotacaoAdmin)