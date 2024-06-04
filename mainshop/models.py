from django.db import models

class MainGadgets(models.Model):
    gadget_image = models.ImageField(upload_to='images/', verbose_name='Upload a picture please')
    gadget_title = models.CharField(max_length=100)

    def __str__(self):
        return self.gadget_title

    class Meta:
        verbose_name = 'Gadgets'
        verbose_name_plural = 'List of gadgets'

class Sales(models.Model):
    sale_title = models.CharField(max_length=100)
    sale_advantage = models.CharField(max_length=100)
    sale_price = models.PositiveIntegerField(default=1000)
    sale_image = models.ImageField(upload_to='images/', verbose_name='Upload a picture please')

    def __str__(self):
        return self.sale_title

    class Meta:
        verbose_name = 'Sales'
        verbose_name_plural = 'List of sales'