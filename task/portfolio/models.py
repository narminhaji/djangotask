from django.db import models

# Create your models here.
class Portfolio(models.Model):
    ad = models.CharField(max_length=20)
    soyad = models.CharField(max_length=20)
    unvan = models.CharField(max_length=50)
    nomre = models.CharField(max_length=20)
    tehsil = models.CharField(max_length=50)
    tecrubeleri = models.TextField()
    bacariqlari = models.TextField()
    hobbi = models.TextField()
    dil_bilikleri = models.CharField(max_length=50)
    is_yeri = models.TextField()

    def __str__(self):
        return self.ad
    

    