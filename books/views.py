from django.shortcuts import render,redirect
from . import models
from .models import Book
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import *
from django.urls import reverse

# Create your views here.
"""Views for the very first page of the library system"""
def index(request):
    return render(request, 'books/index.html')

"""Defining views for the home page"""
@login_required
def home(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'books/home.html', context)

"""Defining views for the search_book page"""
@login_required
def search_book(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = Book.objects.filter(title__icontains=searched)
        context = { 'searched':searched,'books':books }

        return render(request, 'books/search_book.html', context)
    else:
        return render(request, 'books/search_book.html')

"""Defining views for the borrow page"""
@login_required
def borrow(request, book_id):
    clicked = Book.objects.get(id = book_id)
    all_books = Book.objects.all()
    books = Book.objects.filter(title__icontains=clicked)
    context = { 'clicked':clicked, 'books':books, 'all_books':all_books }

    return render(request, 'books/borrow.html', context)

def get_return_date():
  return datetime.today() + timedelta(days = 14)

def book_time_limit():
  return datetime.now() + timedelta(hours=6)

"""Views for the confirm borrow"""
@login_required
def confirm_borrow(request,id):
    book = Book.objects.get(id=id)
    borrower = Borrower(first_name=request.user.first_name,last_name=request.user.last_name,book_name=book.title)
    borrower.save()
 
    requested_book = RequestedBook(book_name = book.title ,pickup_time = book_time_limit(),borrower=request.user)
    requested_book.save()
    book.status = False
    book.save()

    
    return redirect('books:home')



"""Defining views for the profile page"""
@login_required
def profile(request):
    return render(request, 'books/profile.html')

"""Views for the borrowed book"""
@login_required
def borrowed_book(request):
    requested_book = models.RequestedBook.objects.all()
    li = []
    for book in requested_book:
        issuedate = str(book.issued_date.day)+'-'+str(book.issued_date.month)+'-'+str(book.issued_date.year)
        return_date = str(book.return_date.day)+'-'+str(book.return_date.month)+'-'+str(book.return_date.year)

        books = list(models.Book.objects.filter(book_num = book.book_num))
        students = list(models.Borrower.objects.filter(reg_no = book.reg_no))
        i = 0
        for li in books:
            t = (students[i].get_name, students[i].reg_no, books[i].name, books[i].author, issuedate, return_date)
            i += 1
            li.append(t)
        
    return render(request, 'books/borrowed_book.html')
    

"""Views for the returned book"""
@login_required
def returned_book(request):
    return render(request, 'books/returned_book.html')

"""Views for notifications"""
@login_required
def notifications(request):
    issued_book = IssuedBook.objects.all()
    context = {'issued_book':issued_book}
    return render(request, 'books/notifications.html', context)

def borrowed_book(request):
    borrowed = Borrower.objects.all()
    context = {'borrowed':borrowed}
    return render(request,'books/borrowed_book.html', context)






