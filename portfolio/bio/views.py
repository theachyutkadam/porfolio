from django.shortcuts import render
import requests

# Create your views here.
def bio(request):
    return render(request, 'bio.html', {})

def welcome(request):
    response = requests.get('http://localhost:8000/experiance/')
    resume_response = requests.get('http://localhost:8000/resume/')

    experiances = response.json()
    resume = resume_response.json()
    return render(request, 'welcome.html', {'experiances': experiances, 'resume': resume[0], 'flag': True})

