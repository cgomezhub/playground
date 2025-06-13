from django.shortcuts import render

from datetime import date

from django.http import HttpResponse

# from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.


def home(request):
    
    day = date.today()
    
    stack = [{"id": "python", "name": "Python"}, {"id": "php", "name": "PHP"}, {"id": "js", "name": "JS"},  {"id": "java", "name": "Java"}, {"id": "csharp", "name": "C#"}, {"id": "ruby", "name": "Ruby"}, {"id": "go", "name": "Go"}]
    
    return render(request, "landing/landing.html", {
        "description": "This is the landing page of the application.",
        "name": "Juan",
        "age": 44,
        "date": day,
        "stack": stack
    })
    
def stack_detail(request, tool):
    
    return HttpResponse(f"Tecnologia: {tool}")