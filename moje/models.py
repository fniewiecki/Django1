from django.db import models

class ocenaEKG(models.Model):
    numer_zdjecia = models.IntegerField()
    BlokAV_1stopnia = models.BooleanField(default=False)
    RBBB = models.BooleanField(default=False)
    LBBB = models.BooleanField(default=False)
    Bradykardia = models.BooleanField(default=False)
    Tachykardia = models.BooleanField(default=False)
    Trzepotanie = models.BooleanField(default=False)
    Migotanie = models.BooleanField(default=False)
    ZalamekQ = models.BooleanField(default=False)
    BlokAV_2stopnia1 = models.BooleanField(default=False)
    BlokAV_2stopnia2 = models.BooleanField(default=False)
    BlokAV_3stopnia = models.BooleanField(default=False)
    CzyTrudne = models.BooleanField(default=False)

