from django.db import models

# Create your models here.

class Daroo(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to='daroo_images/', blank=True, null=True)  # فیلد تصویر
    price = models.IntegerField()
    category = models.CharField(max_length=50 , null=True)  # این خط را اضافه کن

    def __str__(self):
        return self.title