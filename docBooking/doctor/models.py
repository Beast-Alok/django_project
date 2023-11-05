from django.db import models

# Create your models here.
class Student(models.Model):
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15,default='')

    def __str__(self) -> str:
        return self.name


class Doctor (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    location = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    doc_img = models.ImageField(upload_to='doctor_image',default='')
    def __str__(self) -> str:
        return self.name
