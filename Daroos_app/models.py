from django.db import models

# Create your models here.


class Daroo(models.Model):
    title = models.CharField('عنوان',max_length=60)
    description = models.TextField('توضیحات')
    image = models.ImageField('عکس',upload_to='daroo_images/', blank=True, null=True,)  # فیلد تصویر
    price = models.IntegerField('قیمت')
    category = models.CharField('دسته بندی',max_length=50 , null=True)  # این خط را اضافه کن

    def __str__(self):
        return self.title