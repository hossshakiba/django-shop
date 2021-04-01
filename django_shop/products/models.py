from django.db import models

class Product(models.Model):
    """
    Abstract product model contains common fields among all products
    """
    title = models.CharField('عنوان محصول', max_length=50)
    description = models.TextField('توضیحات')
    cover = models.ImageField('کاور محصول', upload_to=None)
    price = models.PositiveIntegerField('قیمت')
    discount_percent = models.PositiveSmallIntegerField('درصد تخفیف', blank=True, default=0)
    available_count = models.PositiveSmallIntegerField('موجودی انبار')
    is_active = models.BooleanField('فعال/غیرفعال', default=False)


    class Meta:
        abstract = True

    def __str__(self):
        return self.title


