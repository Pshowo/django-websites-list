from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainPageView.as_view(), name='home'),
    path("webstites/", views.Websites.as_view(), name="list"),
    path("webstites/details/", views.WebPage.as_view(), name='details'),
    path("webstites/<int:num>", views.web_detail, name='web_details'),
]