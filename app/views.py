from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse

# Create your views here.

class MainPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app/home.html', {"title":"Main"})

def index(request):
    return HttpResponse("""
    <h1>Websites list</h1>
    """)

class Websites(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app/websites.html', {"title":"Websites"})

class WebPage(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app/web_detail.html', {"title":"Website detail"})        