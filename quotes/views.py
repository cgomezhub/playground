# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
# Create your views here.
from django.shortcuts import render
from django.urls import reverse

day_of_week = [{
    "day": "monday",
    "quote": "Pienso luego existo"
    
},
    {
    "day": "tuesday",
    "quote": "Soy un excelente programador"
    
},
    {
    "day": "wednsday",
    "quote": "La vida es bella"
    
},
    {
    "day": "thursday",
    "quote": "Soy una persona amable"   
    
},
    {
    "day": "friday",
    "quote": "El exito me encuetra en todo lo que hago"
},
    {
    "day": "saturday",
    "quote": "Alegro el dia a quien me saluda"
},
    {
    "day": "sunday",
    "quote": "Reconozco mis erroRes y aprendo de ellos"
},
]

for item_info in day_of_week:
        print(f"Depurando el item desde la vista: {item_info}") 



def index(request):
        
    # for day in days:
    #     path = reverse('day-qoute', args=[day])
    #     list_items += f"<li><a href='{path}'>{day.capitalize()}</a></li>"
        
    # response_html = f"<ul>{list_items}</ul>"
    
    # return HttpResponse(response_html)
    
    return render(request, "quote/quote.html", {
        "description": "This is the Quote page of the application.",
        "days_of_week": day_of_week,
    })



def week_day_with_numbers(request, day):
    
    # day_week = list(day_of_week.keys())
    
    # print(day_week)
    
    if day > len(day_of_week):
        return HttpResponseNotFound("El dia no existe")
    
    # redirect_day = day_of_week[day-1]
    redirect_day = day_of_week[day-1]["day"]
    print(redirect_day)
    
    
    path = reverse('day-qoute', args=[redirect_day])
    
    return HttpResponseRedirect(path)
    # return HttpResponseRedirect(f'/quotes/{day}')
    
def week_day(request, day):
    print(day)
    
    try:
        frase = day_of_week[day_of_week.index(next(item for item in day_of_week if item["day"] == day))]["quote"]
        print(frase)
        return HttpResponse(frase)
    except KeyError:
        # return HttpResponseNotFound("El dia no existe")
        return render(request, "404.html")
        # raise Http404() forma correcta de lanzar un error 404
    except StopIteration:
        # return HttpResponseNotFound("El dia no existe")        return render(request, "../templates/404.html")
        # SE puede usar esto  para renderizar una pagina personalizada
        return render(request, "404.html") 
        # raise Http404() forma correcta de lanzar un error 404
    

    