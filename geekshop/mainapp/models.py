from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    name = models.CharField(verbose_name='категория товара', max_length=255, unique=True)
    description = models.TextField(verbose_name='Описание товара', blank=True, null=True)

    def __str__(self):
        return self.name
