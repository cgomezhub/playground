from django.urls import path
from . import views


urlpatterns = [
    path("", views.index ),
    path("<int:day>", views.week_day_with_numbers ),
    path("<str:day>", views.week_day, name='day-qoute'),
    ]

