from django.db import models

#Create your models here.

class Memoire (models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=100000, decimal_places=2)
    image=models.SlugField(upload_to='images', blank=True)
    slug = models.SlugField(nullt=True)
    actif= models.BooleanField(default=True)

    class Meta:
        verbose_name= ("Memoire")
        verbose_name_prurial=("Memoires")

    def __str__(self):
        return self.name

