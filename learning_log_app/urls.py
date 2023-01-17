from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.topics, name='topics'),
    # Single topic page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Add new topic page
    path('new_topic/', views.new_topic, name='new_topic')
]
