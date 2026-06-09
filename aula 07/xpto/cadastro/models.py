from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)


    def __str__(self):
        return self.nome    


class Curso(models.Model):
    curso = models.CharField(max_length=100)
    turma = models.CharField(max_length=100)
    duracao = models.CharField(max_length=100)

    def __str__(self):
        return self.curso