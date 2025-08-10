from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('votar/', views.votacao_view, name='votacao'),
    path('resultados/', views.resultados_view, name='resultados'),
    path('sucesso/', views.sucesso_view, name='sucesso'),
    path('historico/', views.historico_votacoes_view, name='historico'), # NOVA ROTA
    path('historico/<int:votacao_id>/', views.resultado_especifico_view, name='resultado_especifico'), # NOVA ROTA
]