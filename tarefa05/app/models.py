from django.db import models

# Create your models here.


class postagem(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data = models.DateTimeField  

def __str__(self):
    return self.titulo