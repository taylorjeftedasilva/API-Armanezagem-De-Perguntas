from django.db import models

# Create your models here.

class Game(models.Model):
    pergunta = models.TextField()
    alternativas = models.JSONField()