from django.db import models

# Create your models here.
class admin_proses(models.Model):
    nama = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tgl_uplod = models.DateField()
    file_naskah = models.FileField(upload_to='Naskah/file/')
