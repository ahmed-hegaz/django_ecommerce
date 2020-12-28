from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    PRDName= models.CharField(_("Product name"), max_length=100)
    PRDcategory= models.ForeignKey("Category", verbose_name=_("Category"), on_delete=models.CASCADE, blank= True, null= True)
    PRDbrand= models.ForeignKey("settings.Brand", verbose_name=_("Brand"), on_delete=models.CASCADE, blank= True, null= True)
    PRDDesc= models.TextField(_("Product description"),)
    PRDimage= models.ImageField(_("product image"), upload_to='product/', blank= True, null= True)
    PRDPrice= models.DecimalField(_("Product price"),max_digits=5, decimal_places=2)
    PRDdiscoundPrice= models.DecimalField(_("discound price"),max_digits=5, decimal_places=2)
    PRDCost= models.DecimalField(_("Product cost"),max_digits=5, decimal_places=2)
    PRDCreated= models.DateTimeField(_("Product created"),auto_now_add=False)
    PRDslug= models.SlugField(_("Product url"),blank= True, null= True)
    PRDisnew= models.BooleanField(_("isnew"), default=True)
    PRDbestseller= models.BooleanField(_("bestseller"), default=False)

    def save(self,*args, **kwargs):
        if not self.PRDslug:
            self.PRDslug= slugify(self.PRDName)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")  
# دالة لارجاع رابط صفحة المنتج الواحد
    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"slug": self.PRDslug})
    
   
    def __str__(self):
        return self.PRDName

class ProductImage(models.Model):
    PRDIproduct= models.ForeignKey("Product", verbose_name=_("Product"), on_delete=models.CASCADE)
    PRDIimage= models.ImageField(_("product image"), upload_to='product/')

    

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("Product Images")

    def __str__(self):
        return str(self.PRDIproduct)

class Category(models.Model):
    CATname= models.CharField(_("Category name"), max_length=50)
    CATparent= models.ForeignKey("self", verbose_name=_("Category main"), limit_choices_to= {'CATparent__isnull':True}, on_delete=models.CASCADE, blank=True, null= True)
    CATdsc= models.TextField(_("Category description"))
    CATimg= models.ImageField(_("Category image"), upload_to=None, height_field=None, width_field=None, max_length=None)

    

    class Meta:
        verbose_name = _("Category")

        verbose_name_plural = _("Categorys")


    def __str__(self):
        return self.CATname

class Product_Alternative(models.Model):
    PALMProduct= models.ForeignKey(Product, on_delete=models.CASCADE, related_name= 'main_Product', verbose_name=_("Product"))
    PALMAlternative= models.ManyToManyField("Product",  related_name= 'alternative_product',verbose_name=_("alternative product"))
   

    class Meta:
        verbose_name = _("Product Alternative")

        verbose_name_plural = _("Product Alternatives")


    def __str__(self):
        return str(self.PALMProduct)

class Product_Accessory(models.Model):
    PACCProduct= models.ForeignKey("Product", on_delete= models.CASCADE , related_name= 'mainAccessory_Product', verbose_name=_("Product"))
    PACCAlternative= models.ManyToManyField("Product",  related_name= 'accessories_product',verbose_name=_("accessory product"))
   

    class Meta:
        verbose_name = _("Product Accessory")

        verbose_name_plural = _("Product Accessories")


    def __str__(self):
        return str(self.PACCProduct)








