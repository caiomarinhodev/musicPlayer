from django.db import models


# Create your models here.

class Musica(models.Model):
    nome = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='musicas/')
    banda = models.CharField(max_length=200, blank=True, null=True)
    genero = models.CharField(max_length=100, blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome
