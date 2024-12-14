from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, unique=True, null=False, blank=False, default="00000000000")  
    email = models.EmailField(null=False, blank=False)
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False) 

    class Meta:
        db_table = 'funcionarios'  # Nome personalizado da tabela
   