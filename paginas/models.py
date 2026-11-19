from django.db import models

class filme(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    genero = models.CharField(max_length=100)
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome    

class projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    ano = models.IntegerField()
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        
    )

    def __str__(self):
        return self.nome