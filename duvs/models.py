# Create your models here.
from django.db import models

class Navio(models.Model):
    nome = models.CharField(max_length=100)
    bandeira = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='navios/')

    def __str__(self):
        return self.nome

class DUV(models.Model):
    numero = models.CharField(max_length=50, unique=True, blank=True)  # gerado automaticamente
    data_viagem = models.DateField()
    navio = models.ForeignKey(Navio, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.numero:
            # Formata a data como YYYYMMDD
            data_str = self.data_viagem.strftime('%Y%m%d')

            # Conta quantas DUVs existem para a mesma data (ajuda a gerar sequência)
            duvs_mesma_data = DUV.objects.filter(data_viagem=self.data_viagem).count() + 1

            # Monta o número, ex: DUV-20250629-001
            self.numero = f"DUV-{data_str}-{duvs_mesma_data:03d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"DUV {self.numero} - {self.data_viagem}"

class Passageiro(models.Model):
    TIPO_CHOICES = [
        ('passageiro','Passageiro'),
        ('tripulante',"Tripulante"),
    ]
    duv = models.ForeignKey(DUV,related_name='passageiros',on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20,choices=TIPO_CHOICES)
    nacionalidade = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='passageiros/')
    sid = models.CharField(max_length=50, unique=True, blank=True, null=True)  # Para tripulantes


