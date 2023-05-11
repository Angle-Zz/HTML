from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def post_list(request):
    return render(request, 'blog/Home.html', {})

def redirect_to_login(request):
    return HttpResponseRedirect('/login/')

def redirect_to_register(request):
    return HttpResponseRedirect('/register')

def redirect_to_image_preview(request):
    return HttpResponseRedirect('image-preview')

