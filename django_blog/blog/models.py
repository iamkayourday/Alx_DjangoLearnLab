from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Post model: title, content, author, published_date.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return self.title
