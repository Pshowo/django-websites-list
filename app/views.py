from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse

# Create your views here.

class MainPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html')

def index(request):
    return HttpResponse("""
    <h1>Websites list</h1>
    """)