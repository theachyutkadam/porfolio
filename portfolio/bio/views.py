from django.shortcuts import render

# Create your views here.
def bio(request):
    return render(request, 'bio.html', {})

def welcome(request):
    return render(request, 'welcome.html', {})
