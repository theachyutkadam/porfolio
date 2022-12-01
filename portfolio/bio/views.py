from django.shortcuts import render
import requests

# Create your views here.
def bio(request):
    return render(request, 'bio.html', {})

def welcome(request):
    response = requests.get('http://localhost:8000/experiance/1')
    experiance = response.json()
    # return render(request, 'welcome.html', {
    #               'name': experiance['name'],
    #               'start_date': experiance['start_date'],
    #               'end_date': experiance['end_date']}
    #             )
    return render(request, 'welcome.html', {'role': experiance['role']}
                )
