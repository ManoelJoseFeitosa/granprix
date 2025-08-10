from django.shortcuts import render, redirect
from django.db.models import Sum, Count, F, FloatField, Case, When
from .models import Votacao, Escuderia, Criterio, Voto, Nota

def home_view(request):
    return render(request, 'core/home.html')

def votacao_view(request):
    votacao_ativa = None
    criterios = Criterio.objects.none()
    try:
        votacao_ativa = Votacao.objects.get(esta_ativa=True)
        criterios = votacao_ativa.criterios.order_by('id')
    except Votacao.DoesNotExist:
        votacao_ativa = None

    escuderias = Escuderia.objects.all()

    if request.method == 'POST' and votacao_ativa:
        jurado = request.POST.get('jurado')
        escuderia_id = request.POST.get('escuderia')
        voto = Voto.objects.create(votacao=votacao_ativa, jurado=jurado, escuderia_id=escuderia_id)
        
        for criterio in criterios:
            valor_nota = request.POST.get(f'nota-{criterio.id}')
            if valor_nota:
                Nota.objects.create(voto=voto, criterio=criterio, valor=int(valor_nota))
        return redirect('sucesso')

    contexto = {'votacao_ativa': votacao_ativa, 'escuderias': escuderias, 'criterios': criterios}
    return render(request, 'core/votacao.html', contexto)

# ==================================================================
# VIEW DE RESULTADOS CORRIGIDA
# ==================================================================
def resultados_view(request):
    try:
        votacao_ativa = Votacao.objects.get(esta_ativa=True)
        # CORREÇÃO: trocamos 'voto__' por 'votos_escuderia__' para corresponder ao related_name do modelo
        escuderias = Escuderia.objects.filter(votos_escuderia__votacao=votacao_ativa).annotate(
            total_pontos=Sum('votos_escuderia__notas__valor'),
            num_votos=Count('votos_escuderia', distinct=True)
        ).annotate(
            nota_final=Case(
                When(num_votos__gt=0, then=F('total_pontos') * 1.0 / F('num_votos')),
                default=0.0,
                output_field=FloatField()
            )
        ).order_by('-nota_final')
    except Votacao.DoesNotExist:
        votacao_ativa = None
        escuderias = None

    contexto = {'votacao_ativa': votacao_ativa, 'resultados': escuderias}
    return render(request, 'core/resultados.html', contexto)

# ==================================================================
# VIEW DE RESULTADO ESPECÍFICO CORRIGIDA
# ==================================================================
def resultado_especifico_view(request, votacao_id):
    try:
        votacao = Votacao.objects.get(id=votacao_id)
        # CORREÇÃO: trocamos 'voto__' por 'votos_escuderia__' aqui também
        escuderias = Escuderia.objects.filter(votos_escuderia__votacao=votacao).annotate(
            total_pontos=Sum('votos_escuderia__notas__valor'),
            num_votos=Count('votos_escuderia', distinct=True)
        ).annotate(
            nota_final=Case(
                When(num_votos__gt=0, then=F('total_pontos') * 1.0 / F('num_votos')),
                default=0.0,
                output_field=FloatField()
            )
        ).order_by('-nota_final')
    except Votacao.DoesNotExist:
        votacao = None
        escuderias = None
    
    contexto = {'votacao': votacao, 'resultados': escuderias}
    return render(request, 'core/resultado_especifico.html', contexto)

def historico_votacoes_view(request):
    votacoes_todas = Votacao.objects.order_by('-data_inicio')
    votacao_id_selecionada = request.GET.get('votacao_id')
    votacao_selecionada = None
    lista_votos = Voto.objects.none()
    criterios = Criterio.objects.none()

    if votacao_id_selecionada:
        try:
            votacao_selecionada = Votacao.objects.get(id=votacao_id_selecionada)
        except Votacao.DoesNotExist:
            votacao_selecionada = None
    else:
        votacao_selecionada = votacoes_todas.filter(esta_ativa=True).first()

    if votacao_selecionada:
        criterios = votacao_selecionada.criterios.order_by('id')
        lista_votos = Voto.objects.filter(votacao=votacao_selecionada)\
                                  .select_related('escuderia')\
                                  .prefetch_related('notas__criterio')\
                                  .order_by('jurado')
    
    contexto = {
        'criterios': criterios,
        'votos': lista_votos,
        'votacoes_todas': votacoes_todas,
        'votacao_selecionada': votacao_selecionada,
    }
    
    return render(request, 'core/historico.html', contexto)

def sucesso_view(request):
    return render(request, 'core/sucesso.html')