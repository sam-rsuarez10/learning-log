from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.topics, name='topics'),
    # Single topic page
    path('topics/<int:topic_id>/', views.topic, name='topic')
]
