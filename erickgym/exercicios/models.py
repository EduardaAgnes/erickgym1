from django.db import models

class Alunos(models.Model):
    SEXO_CHOICES = (
        ('masculino','MASCULINO'),
        ('feminino','FEMININO')
    )

    nome = models.CharField(max_length=60)
    foto = models.ImageField(null = True, blank = True)
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=60)
    dt_nasc = models.CharField(max_length=60)
    telefone = models.PositiveIntegerField()
    cpf = models.PositiveIntegerField()

    def __str__(self):
        return self.nome