from django.db import models

# Create your models here.

class Topic(models.Model):
    ''' A topic the user is learning about '''
    topic_name = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        ''' String representation of the model '''
        return self.topic_name

class Entry(models.Model):
    ''' A entry journal of a specific topic '''
    text = models.TextField(help_text='Today I learned...')
    date_added = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        return self.text[:50] + '...'
