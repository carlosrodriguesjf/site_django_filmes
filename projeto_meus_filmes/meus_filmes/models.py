from django.db import models

class Filme(models.Model):
    filme = models.TextField(max_length=255)
    assistido = models.BooleanField(default=False)
    genero = models.TextField(max_length=255)

