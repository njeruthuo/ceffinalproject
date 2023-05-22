from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-update_date', '-pub_date']

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blogs', null=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
