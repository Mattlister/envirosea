from django.shortcuts import render, redirect

# Create your views here.


def view_book(request):
    """ A view that adds people to booking """

    return render(request, 'book/book.html')


def add_person(request, item_id):
    """ Add a quantity of people to the booking """

    quantity1 = int(request.POST.get('quantity1'))

    redirect_url = request.POST.get('redirect_url')
    book = request.session.get('book', {})

    if item_id in list(book.keys()):
        book[item_id] += quantity1
    else:
        book[item_id] = quantity1

    request.session['book'] = book
    print(request.session['book'])
    return redirect(redirect_url)
