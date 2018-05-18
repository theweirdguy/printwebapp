from django.urls import path
from . import views

urlpatterns = [
    path('print', views.some_view, name='printing'),
    path('', views.data_view, name='index'),

]

