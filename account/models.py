from django.db import models

# Create your models here.
class CustumersSighnUp(models.Model):
    name     = models.CharField(null=False,blank=False,max_length=50)
    username =models.CharField(null=False,blank=False ,max_length=50)
    emial    = models.EmailField(null=False,blank=False)
    password = models.CharField(null=False,blank=False,max_length=50)
    check1    = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.emial

