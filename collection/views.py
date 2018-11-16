from django.shortcuts import render, redirect
from collection.forms import ClimbingShoeForm
from collection.models import ClimbingShoe


# Create your views here.
def index(request):
    climbingshoes = ClimbingShoe.objects.all()
    return render(request, 'index.html', {
        'climbingshoes': climbingshoes,
    })


def climbingshoe_detail(request, slug):
    climbingshoe = ClimbingShoe.objects.get(slug=slug)
    return render(request, 'climbingshoes/climbingshoe_detail.html', {
        'climbingshoe': climbingshoe
    })


def edit_climbingshoe(request, slug):
    climbingshoe = ClimbingShoe.objects.get(slug=slug)
    form_class = ClimbingShoeForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=climbingshoe)
        if form.is_valid():
            form.save()
            return redirect('climbingshoe_detail', slug=climbingshoe.slug)
    else:
        form = form_class(instance=climbingshoe)
    return render(request, 'climbingshoes/edit_climbingshoe.html', {
        'climbingshoe': climbingshoe,
        'form': form,
    })
