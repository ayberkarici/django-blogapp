from django.db import models
from django.utils.text import slugify

    
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    description = models.TextField()
    isActive = models.BooleanField(default=True)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True, db_index=True, editable=False)
    categories = models.ManyToManyField(Category, blank=True)
    #category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE ) # null=True, on_delete=models.SET_NULL , default=1, on_delete=models.SET_DEFAULT
    
    def __str__(self):
        return f"{self.title}"  
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
