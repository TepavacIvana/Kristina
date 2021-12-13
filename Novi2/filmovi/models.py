from django.db import models

# Create your models here.


class Produkcija(models.Model):
    produkcijske_kuce = models.CharField(max_length=200)

    def __str__(self):
        return self.produkcijske_kuce


class Bioskopi(models.Model):
    bioskop = models.CharField(max_length=50)

    def __str__(self):
        return self.bioskop


class Filmovi(models.Model):
    naslovi = models.CharField(max_length=300)
    zanrovi = models.CharField(max_length=100)
    rezija = models.CharField(max_length=200)
    glumci = models.CharField(max_length=300)
    ocene = models.IntegerField()
    produkcija = models.ForeignKey(Produkcija, related_name='filmovi', on_delete=models.CASCADE)
    biskis = models.ForeignKey(Bioskopi, related_name='filmovi', on_delete=models.CASCADE)

    def __str__(self):
        return self.naslovi

