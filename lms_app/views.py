from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import BookForm, CategoryForm

# Create your views here.

def index(request):
    if request.method =='POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
            return redirect('/')
            
            
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()    
            
            
    
      
            
    
    
    context = {
        'category': Category.objects.all(),
        'books':Book.objects.all(),
        'form': BookForm(),
        'formcat':CategoryForm(),
        'allbooks': Book.objects.filter(active=True).count(),
        'bookssold': Book.objects.filter(status = 'sold').count(),
        'booksrental': Book.objects.filter(status = 'rental').count(),
        'booksavailble': Book.objects.filter(status = 'availble').count(),
    }
    return render(request, 'pages/index.html',context)
    
    
    
    
def books(request):
    context = {
        'category': Category.objects.all(),
        'books':Book.objects.all(),
        'formcat':CategoryForm(),
        
    }
    return render(request, 'pages/books.html', context)
    
    
    
    
    
    
    
    
    
def delete(request, id):
    book_delete= get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    
    
    return render(request, 'pages/delete.html')
    
    
    
    
    
    
    
    
    
def update(request, id):
    book_id= Book.objects.get(id = id)
    if request.method == 'POST':
        book_save = BookForm(request.POST , request.FILES , instance = book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance = book_id)
            
    context = {
        'form':book_save,
    }
        
    return render(request, 'pages/update.html', context)
            
            
      
    
    
    
    
    
