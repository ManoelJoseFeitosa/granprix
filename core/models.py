from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# MODELO ATUALIZADO
class Votacao(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    data_inicio = models.DateTimeField(auto_now_add=True)
    esta_ativa = models.BooleanField(default=True)
    
    # ==========================================================
    # LINHA ADICIONADA PARA CRIAR O VÍNCULO DIRETO
    # ==========================================================
    criterios = models.ManyToManyField('Criterio', verbose_name="Critérios da Votação")

    def __str__(self):
        return self.nome

class Escuderia(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nome

class Criterio(models.Model):
    titulo = models.CharField(max_length=100)
    pergunta = models.TextField()
    peso_maximo = models.PositiveIntegerField()
    
    def __str__(self):
        return self.titulo

class Voto(models.Model):
    votacao = models.ForeignKey(Votacao, on_delete=models.CASCADE, related_name='votos')
    jurado = models.CharField(max_length=100)
    escuderia = models.ForeignKey(Escuderia, on_delete=models.CASCADE, related_name='votos_escuderia') # Adicionado related_name para clareza
    data_votacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Voto de {self.jurado} para {self.escuderia.nome} na votação '{self.votacao.nome}'"

class Nota(models.Model):
    voto = models.ForeignKey(Voto, on_delete=models.CASCADE, related_name='notas')
    criterio = models.ForeignKey(Criterio, on_delete=models.CASCADE)
    valor = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.criterio.titulo}: {self.valor}"