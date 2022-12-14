from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    no = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    nim = models.CharField(max_length=50)
    ttl = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='galeri/',blank=True, null=True)

def __str__(self):
    return self.no