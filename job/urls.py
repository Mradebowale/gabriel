from django.urls import path
from .views import home, jobuploads

urlpatterns = [
    path("", home, name="home"),
    path("jobs/", jobuploads, name="jobs")
]