from django.shortcuts import render

# Create your views here.
def index(request):
    number = 6
    thing = "Sean Houde"
    return render(request, 'index.html', {
        'number': number,
        'thing': thing,
    })
