from django.db import models

# Create your models here.
class Part(models.Model):
    title = models.CharField(max_length=60)
    price = models.FloatField()
    desc = models.TextField(max_length=1024)
    def __str__(self):
        return self.title

class Contact(models.Model):
    name        = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=13)
    email       = models.EmailField()
    message     = models.TextField()
    def __str__(self):
        return self.name
class Subscribes(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email

class News (models.Model):
    title       = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.title