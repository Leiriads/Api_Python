from django.db import models
from uuid import uuid4

# Create your models here.

class Alunos(models.Model):
    id_aluno = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255)
    idade = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)