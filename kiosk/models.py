from django.db import models
from django.urls import reverse

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(verbose_name="SLUG", unique=True, allow_unicode=True)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    inventory = models.IntegerField(default=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='MENU_IMAGE')

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural ='menus'
        db_table = 'kiosk_menus'
        ordering = ('price',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('blog:menu_detail', args=(self.slug,))