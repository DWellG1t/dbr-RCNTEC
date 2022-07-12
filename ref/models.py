from pyexpat import model
from django.db import models

# Create your models here.

class case(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    solution = models.TextField('Решение')
    full = models.TextField('Полное решение')
    date = models.DateField('Дата')
    def __str__(self):
        return self.title

class tipsMod(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    tip = models.TextField('Совет')
    def __str__(self):
        return self.title


        

