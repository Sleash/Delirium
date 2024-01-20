from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('submit/', views.StreakCreate.as_view(), name='submit'),
    path('<character>/<goal>/', views.StreakingView.as_view(), name='streakingcg'),
    path('', RedirectView.as_view(url='all/all/', permanent=True), name='streaking'),
]