from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainPageView.as_view()),
    path("webstites/", views.index, name='index' )
]