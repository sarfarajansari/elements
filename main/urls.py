from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("",views.index, name="index"),
    path("error/",views.error,name="error"),
    path("search/",views.search,name="search")
]
