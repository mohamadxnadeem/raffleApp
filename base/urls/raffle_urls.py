from django.urls import path
from base.views import raffle_views as views


urlpatterns = [
    path('all/', views.getRaffles, name='rafffles'),
   

]