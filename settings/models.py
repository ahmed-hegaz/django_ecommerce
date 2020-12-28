from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Brand(models.Model):
    BRDname= models.CharField( max_length=50)
    BRDdesc= models.TextField(blank=True, null=True)
    

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.BRDname

class Variant(models.Model):
    VARname= models.CharField( max_length=50)
    VARdesc= models.TextField(blank=True, null=True)
    

    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        return self.VARname



