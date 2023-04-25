from django.db import models


class Asosiy_rasm(models.Model):
    rasm1 = models.ImageField(upload_to='jamoa_rasm')
    rasm2 = models.ImageField(upload_to='jamoa_rasm')
    rasm3 = models.ImageField(upload_to='jamoa_rasm')

class Statistika(models.Model):
    nomi = models.CharField(max_length=100)
    soni = models.FloatField()
    

class Tarif(models.Model):
    nomi = models.CharField(max_length=100)
    malumot  = models.TextField()
    rasm = models.ImageField(upload_to='jamoa_rasm')

class Jamoa(models.Model):
    nomi = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='jamoa_rasm')
    rasm1 = models.ImageField(upload_to='jamoa_rasm')
    rasm2 = models.ImageField(upload_to='jamoa_rasm')
    rasm3 = models.ImageField(upload_to='jamoa_rasm')
    jamoa_haqida = models.TextField()

class Xizmatlar(models.Model):
    rasm = models.ImageField(upload_to='jamoa_rasm')
    rasm2 = models.ImageField(upload_to='jamoa_rasm')

class Xususiyat(models.Model):
    nomi = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to='jamoa_rasm')
    

class Boglanish(models.Model):
    nomer = models.IntegerField()
    link = models.CharField(max_length=100)
    joy_nomi = models.CharField(max_length=100)

class Malumot(models.Model):
    malumot = models.CharField(max_length=100)