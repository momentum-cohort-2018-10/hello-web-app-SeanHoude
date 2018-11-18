from django.shortcuts import render, redirect
from collection.forms import ClimbingShoeForm
from collection.models import ClimbingShoe
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404


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


@login_required
def edit_climbingshoe(request, slug):
    climbingshoe = ClimbingShoe.objects.get(slug=slug)
    if climbingshoe.user != request.user:
        raise Http404
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

def create_climbingshoe(request):
    form_class = ClimbingShoeForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            climbingshoe = form.save(commit=False)
            climbingshoe.user = request.user
            climbingshoe.slug = slugify(climbingshoe.name)
            climbingshoe.save()
            return redirect('climbingshoe_detail', slug=climbingshoe.slug)
    else:
        form = form_class()

    return render(request, 'climbingshoes/create_climbingshoe.html', {
        'form': form,
    })

def browse_by_name(request, initial=None):
    if initial:
        climbingshoe = ClimbingShoe.objects.filter(
            name__istartswith=initial).order_by('name')
    else:
        climbingshoes = ClimbingShoe.objects.all().order_by('name')

    return render(request, 'search/search.html', {
        'climbingshoes': climbingshoes,
        'initial': initial,
    })


