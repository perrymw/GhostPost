"""
Boast or Roast
Content
upvote/downvote
datetime
Delete
"""
from django.db import models
from django.utils import timezone

class BoastandRoast(models.Model):
    boast = models.BooleanField(default=True)
    content = models.TextField()
    upordown = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    total = models.IntegerField(default=0)
    prideorhide = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.content}"