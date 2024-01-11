from django.urls import path

from polls.views.demo import Demo


urlpatterns = [
    path(route='demo', view=Demo.as_view())
]
