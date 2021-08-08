from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.http.response import HttpResponse
from .models import Website
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class MainPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app/home.html', {"title":"Main"})

def index(request):
    return HttpResponse("""
    <h1>Websites list</h1>
    """)

class Websites(ListView):

        queryset = Website.objects.all().order_by('alexa_rank')
        paginate_by = 25
        context_object_name = 'websites'
        template_name = "app/websites.html"
        # return render(request, 'app/websites.html', {"title":"Websites", "websites":websites})

class WebPage(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app/web_detail.html', {"title":"Website detail"})        

def web_detail(request, num):
    web = Website.objects.filter(id=num).first()
    context = {"web": web}
    return render(request, 'app/web_detail.html', context)