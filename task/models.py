from django.db import models

class Task(models.Model):
    titulo = models.CharField(max_length=155)
    descricao = models.TextField(blank=True)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
