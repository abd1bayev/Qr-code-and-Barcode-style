from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File


class Product(models.Model):
    name = models.CharField(max_length=200)
    barcode = models.ImageField(upload_to='images/', blank=True)
    country_code = models.CharField(max_length=3, null=True)
    manufacturer_code = models.CharField(max_length=5, null=True)
    product_code = models.CharField(max_length=5, null=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.pk:
            EAN = barcode.get_barcode_class('ean13')
            ean = EAN(f'0{self.country_code}{self.manufacturer_code}{self.product_code}', writer=ImageWriter())
            with BytesIO() as buffer:
                ean.write(buffer)
                self.barcode.save(f'{self.name}.png', File(buffer), save=False)
        return super().save(*args, **kwargs)