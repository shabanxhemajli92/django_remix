from django.urls import path
from .views import index,new_reminder

urlpatterns=[
    path("",index),
    path("new-reminder/",new_reminder)
]