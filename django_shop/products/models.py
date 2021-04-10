from django.db import models
from django.contrib.postgres.fields import ArrayField

class Product(models.Model):
    """
    Abstract product model contains common fields among all products
    TODO:
        - cateogries
        - gallery
    """
    title = models.CharField('عنوان محصول', max_length=50)
    description = models.TextField('توضیحات')
    cover = models.ImageField('کاور محصول', upload_to=None)
    price = models.PositiveIntegerField('قیمت')
    discount_percent = models.PositiveSmallIntegerField('درصد تخفیف', blank=True, default=0)
    available_count = models.PositiveSmallIntegerField('موجودی انبار')
    technical_details = models.JSONField('مشخصات فنی')
    attributes = ArrayField(
        'امکانات محصول',
        models.CharField(max_length=100, blank=True),
        blank = True, null = True)
    is_active = models.BooleanField('فعال/غیرفعال', default=False)


    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    @property
    def final_price(self):
        """Calculate the final price of product with discount"""
        final_price = self.price * (100 - self.discount) / 100
        return final_price

    @property
    def is_available(self):
        """Returns True if the product is available"""
        if self.availlable_count > 0:
            return True
        return False

