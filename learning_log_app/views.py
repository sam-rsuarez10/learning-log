from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm

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

def new_topic(request):
    ''' Display topic's form and save it into the database '''
    if request.method == 'GET':
        # User have not entered data yet
        # Create blank form
        form = TopicForm()
        return render(request, 'learning_log_app/new_topic.html', {'form': form})
    else:
        # User entered data, proccess it and save it into db
        form = TopicForm(request.POST) # populated form with user data
        if form.is_valid():
            form.save() # save into database
            return redirect('/topics')
