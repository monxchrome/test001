from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length= 50)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.id}: {self.title}"