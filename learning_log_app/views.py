from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.


def index(request):
    return render(request, 'learning_log_app/index.html')

@login_required
def topics(request):
    ''' Show all topics created '''
    topics_created = Topic.objects.order_by('date_added')
    context = {'topics': topics_created}
    return render(request, 'learning_log_app/topics.html', context)

@login_required
def topic(request, topic_id):
    ''' Show topic entries given the topic id'''
    # select given topic
    topic = Topic.objects.get(id=topic_id)
    # select entries from corresponding topic
    entries = topic.entry_set.order_by('-date_added')

    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_log_app/topic.html', context)

@login_required
def new_topic(request):
    ''' Display topic's form and save it into the database '''
    if request.method == 'GET':
        # User have not entered data yet
        # Create blank form
        form = TopicForm()
    else:
        # User entered data, proccess it and save it into db
        form = TopicForm(request.POST) # populated form with user data
        if form.is_valid():
            form.save() # save into database
            return redirect('learning_logs:topics')
    return render(request, 'learning_log_app/new_topic.html', {'form': form})

@login_required
def new_entry(request, topic_id):
    '''Add new entry to the corresponding topic'''
    topic = Topic.objects.get(id=topic_id)
    if request.method == 'GET':
        # User have not entered data yet, create blank form
        form = EntryForm()
        context = {'form': form, 'topic': topic}
    else:
        # User entered data, proccess it and save it into db
        form =  EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False) # create new instance of Entry
            entry.topic = topic # connect entry with corresponding topic
            entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    return render(request, 'learning_log_app/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic =  entry.topic
    if request.method == 'GET':
        # User have not entered new data
        # populate form with existing entry data
        form = EntryForm(instance=entry)
        context = {'topic': topic, 'entry': entry, 'form': form}
    else:
        # User edited the existing entry
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    return render(request, 'learning_log_app/edit_entry.html', context)