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
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    total = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.content}"