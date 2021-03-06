from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=200)

    class Meta: 
        ordering = ('name', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_images', blank=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateField(blank=True)
    quantity = models.IntegerField(blank=True)

    class Meta: 
        ordering = ('name', )
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    

    def __str__(self):
        return f'{self.name}'