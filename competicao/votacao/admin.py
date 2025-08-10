from django.contrib import admin
from .models import Escuderia, Voto

admin.site.register(Escuderia)
admin.site.register(Voto) # Para podermos ver os votos também