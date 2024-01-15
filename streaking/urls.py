from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('<character>/<goal>/', views.StreakingView.as_view(), name='streakingcg'),
    path('', RedirectView.as_view(url='all/all/', permanent=True)),
]