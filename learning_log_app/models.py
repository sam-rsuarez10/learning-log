from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    ''' A topic the user is learning about '''
    topic_name = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        ''' String representation of the model '''
        return self.topic_name

class Entry(models.Model):
    ''' A entry journal of a specific topic '''
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        return self.text[:50] + '...'
