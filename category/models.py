from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name_plural = 'categories'