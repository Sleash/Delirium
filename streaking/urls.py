from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('submit/', views.StreakCreate.as_view(), name='submit'),
    path('p/<player>/', views.StreakingView.as_view(), name='streakingp'),
    path('all/all/', RedirectView.as_view(pattern_name='streaking', permanent=True), name='streakingaa'),
    path('<character>/<goal>/', views.StreakingView.as_view(), name='streakingcg'),
    path('', views.StreakingView.as_view(), name='streaking'),
]