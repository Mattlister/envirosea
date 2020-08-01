from django.shortcuts import render

# Create your views here.


def oceans(request):
    """ View to return oceans page """
    return render(request, 'ocean/oceans.html')
