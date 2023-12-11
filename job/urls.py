from django.urls import path
from .views import home, jobuploads, logins, applynow

urlpatterns = [
    path("", home, name="home"),
    path("jobs/", jobuploads, name="jobs"),
    path("login/", logins, name="login"),
    path("apply/", applynow, name="apply")
]