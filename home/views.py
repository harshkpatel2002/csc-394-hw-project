from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print("HelloWorld")
    return render(request, "index.html")

def process_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        interest = request.POST['interest']
        time_of_day = request.POST['timeOfDay']
        # Send to GPT API
        return HttpResponse("Responses Submitted")
    return render(request, 'index.html')