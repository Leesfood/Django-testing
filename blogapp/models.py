from django.db import models
from django.contrib.auth.models import User
from django.db.models import SET_NULL

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField()
    trending = models.BooleanField(default=False)
    writer = models.ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    slug =models.SlugField(default="slug")

    def __str___(self):
        return self.title
