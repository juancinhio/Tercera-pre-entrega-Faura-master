from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import home

app_name = "home"

urlpatterns = [
    path("", home, name="home"),

]

urlpatterns += staticfiles_urlpatterns()