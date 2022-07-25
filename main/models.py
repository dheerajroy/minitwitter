from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    image = models.ImageField(upload_to='tweet_images', blank=True, null=True)
    description = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.description}'
