from django.shortcuts import render
from .models import Topic, Entry

# Create your views here.


def index(request):
    return render(request, 'learning_log_app/index.html')

def topics(request):
    ''' Show all topics created '''
    topics_created = Topic.objects.order_by('date_added')
    context = {'topics': topics_created}
    return render(request, 'learning_log_app/topics.html', context)

def topic(request, topic_id):
    ''' Show topic entries given the topic id'''
    # select given topic
    topic = Topic.objects.get(id=topic_id)
    # select entries from corresponding topic
    entries = topic.entry_set.order_by('-date_added')

    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_log_app/topic.html', context)
