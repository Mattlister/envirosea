from django.shortcuts import render

# Create your views here.


def view_book(request):
    """ View to renders the book contents page"""

    return render(request, 'book/book.html')
