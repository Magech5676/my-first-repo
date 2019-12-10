from django.http import HttpResponseRedirect
from django.conf import settings
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]