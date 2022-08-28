from django.urls import path
from base.views import prize_views as views


urlpatterns = [
    path('all/', views.getPrizes, name='prizes'),
   
]