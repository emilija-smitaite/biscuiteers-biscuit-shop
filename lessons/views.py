from django.shortcuts import render


def classes(request):
    """ A view to return the index page """

    return render(request, 'lessons/classes.html')
