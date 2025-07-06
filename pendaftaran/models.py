from django.db import models

class Hotel(models.Model):
    nama = models.CharField(max_length=100)
    kamar = models.CharField(max_length=50)
    harga = models.IntegerField()
    lama_inap = models.IntegerField()

    def __str__(self):
        return self.nama
