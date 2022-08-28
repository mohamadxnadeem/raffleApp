from django.urls import path
from base.views import customer_views as views


urlpatterns = [
    path('all/', views.getCustomers, name='customers'),

]