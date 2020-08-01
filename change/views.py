from django.shortcuts import render

# Create your views here.


def change(request):
    """ View to return change page """
    return render(request, 'change/why.html')
