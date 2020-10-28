from django.db import models

# Create your models here.
class Hero(models.Model):
    title = models.CharField(blank = False ,null=False,max_length=30) #models.CharFieldは、文字列を入力できる型
    text = models.TextField(blank = True)
    created_datetime = models.DateTimeField(blank = False,null=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images',blank=True,null=True)

    def __str__(self):
        return self.title