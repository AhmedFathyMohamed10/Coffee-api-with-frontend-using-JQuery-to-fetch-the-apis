from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

class CoffeeImageModel(models.Model):
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='coffee_images/', null=True, blank=True)

    def __str__(self):
        return self.coffee.name


def pre_save_coffee_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

pre_save.connect(pre_save_coffee_receiver, sender=Coffee)