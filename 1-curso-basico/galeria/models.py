from django.db import models

# Django ORM
class Fotografia(models.Model):
    # precisa ser uma tupla para o Charfield entender
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False) # coluna do tipo string
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"Fotografia: [nome={self.nome}]"