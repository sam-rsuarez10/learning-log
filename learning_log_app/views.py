from django.shortcuts import render
from .models import Topic

# Create your views here.


def index(request):
    return render(request, 'learning_log_app/index.html')

def topics(request):
    ''' Show all topics created '''
    topics_created = Topic.objects.order_by('date_added')
    context = {'topics': topics_created}
    return render(request, 'learning_log_app/topics.html', context)
