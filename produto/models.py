from django.db import models
from django.utils import timezone

# Create your models here.

CATEGORY_LIST = (
    ("TECNOLOGIA", "Tecnologia"),
    ("ALIMENTO", "Alimento"),
    ("CASA", "Casa"),
    ("LAZER", "Lazer"),
    ("JARDINAGEM", "Jardinagem"),
    ("CONSTRUCAO", "Construção"),
    ("OUTROS", "Outros"),
)

class Produto(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_LIST)
    price = models.FloatField()
    desc = models.TextField(max_length=1000)
    thumb = models.ImageField(upload_to='products_thumb')
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name








