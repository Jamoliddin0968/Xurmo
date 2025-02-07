from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Категория номи")
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name="Фон расм")
    description = models.TextField(blank=True, null=True, verbose_name="Тавсиф")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Яратилган сана")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категориялар"
        ordering = ['name']

    