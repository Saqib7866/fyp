from django.db import models


class Tweet(models.Model):
    message = models.TextField()
    urgent = models.BooleanField(default=False)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
