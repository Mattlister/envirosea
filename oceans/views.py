from django.shortcuts import render

# Create your views here.


def oceans(request):
    """ View to return change page """
    return render(request, 'oceans/oceans.html')
