from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator


# Товар для нашей витрины
class New(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()


    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',
    )
    data_public = models.DateTimeField(null=True,auto_now_add=True)

    def __str__(self):
        return f'{self.name.title()} {self.data_public.date()} {self.description}'



class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()