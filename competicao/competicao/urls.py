from django.contrib import admin
from django.urls import path, include  # Apenas 'include' é necessário aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),    # Esta linha direciona tudo para o seu app
]