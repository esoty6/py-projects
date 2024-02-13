from django.urls import path
from polls.views.demo import Demo
from polls.views.demo2 import Demo2


urlpatterns = [
    path(route='demo', view=Demo.as_view()),
    path(route='demo2', view=Demo2.as_view())
]
