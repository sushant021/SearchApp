from django.shortcuts import render,get_object_or_404
from .models import Book,Author
import json
from django.http import HttpResponse

def index(request):
    if request.method=='POST':
        search_query = request.POST.get('txtSearch','')
        books = Book.objects.all()
        book_set = []
        for book in books:
            if search_query in book.title.lower() or search_query in book.author.name.lower():
                book_set.append(book)
    else:
        book_set = Book.objects.all()
    
    return render(request,'SearchApp\index.html',{'book_set':book_set})

def autocompleteBook(request):
    query_term = request.GET.get('term','')
    result_books = Book.objects.filter(title__contains=query_term)
    results = []
    for book in result_books:
        results.append(book.title)
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
