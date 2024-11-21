from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', views.home, name='bl-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('video/', views.video, name='bl-video'),
    path('marketplace/', views.marketplace, name='bl-marketplace'),  
    path('groups/', views.groups, name='bl-groups'),
    path('gaming/', views.gaming, name='bl-gaming'),
    path('logout/', views.logout_view, name='logout'),
    path('create_event/', views.create_event, name='create_event'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),  # Add event detail view
    path('event/<int:event_id>/rsvp/', views.rsvp_event, name='rsvp_event'),
    path('events/', views.event_list, name='event_list'),
    
]