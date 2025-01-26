from django.conf import settings
from django.db import models
from django.utils import timezone


class Rating(models.Model):
    rating = models.CharField(max_length=100)


class Tag(models.Model):
    tag = models.CharField(max_length=100)


class posts_with_tag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tags')


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    claim = models.CharField(max_length=500)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title