from django.contrib import admin
from django.urls import path, include
from core import views  # IMPORTANTE: Adicione esta linha para importar as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),    # Esta linha direciona tudo para o seu app
]