from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Escuderia(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Voto(models.Model):
    jurado = models.CharField(max_length=100)
    escuderia = models.ForeignKey(Escuderia, on_delete=models.CASCADE)
    data_votacao = models.DateTimeField(auto_now_add=True)

    # Nossos 7 critérios de avaliação
    aderencia = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    criatividade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    inovacao = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(15)])
    atratividade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    canvas = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    prototipo = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    pitch = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)])

    def __str__(self):
        return f"Voto de {self.jurado} para {self.escuderia.nome}"
