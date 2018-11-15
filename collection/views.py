from django.shortcuts import render
from collection.models import ClimbingShoe

# Create your views here.
def index(request):
    ClimbingShoes = ClimbingShoe.objects.all()
    return render(request, 'index.html', {
        'ClimbingShoes': ClimbingShoes,
    })

def climbingshoe_detail(request, slug):
    climbingshoe = ClimbingShoe.objects.get(slug=slug)
    return render(request, 'climbingshoes/climbingshoe_detail.html', {
        'climbingshoe': climbingshoe
    })
    # number = 6
    # thing = "Sean Houde"
    # return render(request, 'index.html', {
    #     'number': number,
    #     'thing': thing,
    # })
