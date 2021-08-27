from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from localizacao.models import Localizacao




class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def descricao_completa2(self):
        return '%s - %s ' % (self.nome, self.descricao)

    def __str__(self):
        return self.nome