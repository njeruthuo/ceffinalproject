from django.db import models
from django.utils import timezone
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
    image = models.ImageField(upload_to='images', blank=True, null=True)
    video = models.ImageField(upload_to='videos', blank=True, null=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    # views = models.IntegerField(default=0)


class Event(models.Model):
    EVENT_CATEGORIES = [
        ('system', 'System Event'),
        ('security', 'Security Event'),
        ('application', 'Application Event'),
        ('network', 'Network Event'),
        ('data', 'Data Event'),
        ('performance', 'Performance Event'),
        ('change', 'Change Event'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    image = models.URLField(blank=True, null=True)
    organizer = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=EVENT_CATEGORIES)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, default=200, null=True, blank=True)
    registration_link = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    @staticmethod
    def delete_expired_events():
        expired_events = Event.objects.filter(end_date__lt=timezone.now())
        expired_events.delete()


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Galleries'


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
