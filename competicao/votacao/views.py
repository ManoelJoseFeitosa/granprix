from django.shortcuts import render, redirect
from .models import Escuderia, Voto
from django.db.models import Avg, F

def votacao_view(request):
    if request.method == 'POST':
        # Salvar os dados do formulário no banco de dados
        jurado = request.POST.get('jurado')
        escuderia_id = request.POST.get('escuderia')
        escuderia = Escuderia.objects.get(id=escuderia_id)

        Voto.objects.create(
            jurado=jurado,
            escuderia=escuderia,
            aderencia=request.POST.get('aderencia'),
            criatividade=request.POST.get('criatividade'),
            inovacao=request.POST.get('inovacao'),
            atratividade=request.POST.get('atratividade'),
            canvas=request.POST.get('canvas'),
            prototipo=request.POST.get('prototipo'),
            pitch=request.POST.get('pitch'),
        )
        return redirect('sucesso') # Redireciona para a página de sucesso

    escuderias = Escuderia.objects.all()
    contexto = {'escuderias': escuderias}
    return render(request, 'votacao/votacao.html', contexto)

def resultados_view(request):
    # Consulta para calcular a nota final
    resultados = Escuderia.objects.annotate(
        media_aderencia=Avg('voto__aderencia'),
        media_criatividade=Avg('voto__criatividade'),
        media_inovacao=Avg('voto__inovacao'),
        media_atratividade=Avg('voto__atratividade'),
        media_canvas=Avg('voto__canvas'),
        media_prototipo=Avg('voto__prototipo'),
        media_pitch=Avg('voto__pitch'),
    ).annotate(
        nota_final=F('media_aderencia') + F('media_criatividade') + F('media_inovacao') +
                   F('media_atratividade') + F('media_canvas') + F('media_prototipo') +
                   F('media_pitch')
    ).order_by('-nota_final') # Ordena do maior para o menor

    contexto = {'resultados': resultados}
    return render(request, 'votacao/resultados.html', contexto)

def sucesso_view(request):
    return render(request, 'votacao/sucesso.html')
