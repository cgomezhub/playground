from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.db.models import Q
from django.core.paginator import Paginator


from minilibrary.models import Book

# Create your views here.
def index(request):
    
    books = Book.objects.all()
    query = request.GET.get('query_search')
    query_start = request.GET.get('start')
    query_end = request.GET.get('end')
    
    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(author__name__icontains=query)
            
        )
        
    if query_start and query_end:
        books = books.filter(
            publication_date__range=[query_start, query_end]
        )
    
    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    query_params = request.GET.copy()
    if 'page' in query_params:
        query_params.pop('page', None)
        
    query_string = query_params.urlencode()
        
                
    
    try:    
        return render(request, 'minilibrary/minilibrary.html', {
            "name":"Carlos",
            "query": query,
            "page_obj": page_obj,
            "query_start": query_start,
            "query_end": query_end,
            "query_string": query_string
            
        })
    except Exception as e:
        return HttpResponseNotFound("Página no encontrada")


