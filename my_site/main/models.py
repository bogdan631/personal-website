from django.db import models

# Create your models here.

class Table(models.Model):
    text = models.TextField('Заявка')
    def __str__(self): return self.text
    class Meta():
        verbose_name='Заявка'
        verbose_name_plural = 'Заявки'