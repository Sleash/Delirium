from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('top', views.TopView.as_view(), name='top'),
    path('votedata', views.votedata, name='votedata'),
    path('scoredata', views.scoredata, name='scoredata')
]