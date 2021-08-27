from django.db import models



class Atracao(models.Model):
    TIPO = (
        ('e', 'Entreterimento'),
        ('l', 'Lazer'),
        ('a', 'Arte'),
        ('m', 'Musica'),

    )

    nome = models.CharField(max_length=150)
    endereco = models.TextField()
    descricao = models.TextField()
    horario = models.IntegerField()
    tipo = models.CharField(max_length=1, choices=TIPO)

    def __str__(self):
        return self.nome

