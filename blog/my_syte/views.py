from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'my_syte/home_page.html')

def posts(request):
    pass

def post_ditails(request):
    pass