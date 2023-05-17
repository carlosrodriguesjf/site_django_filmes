from django.db import models

class Filme(models.Model):
    filme = models.TextField(max_length=255)
    lido = models.BooleanField(default=False)
    resenha = models.TextField(max_length=255)

