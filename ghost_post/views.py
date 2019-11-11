from django.shortcuts import render,HttpResponseRedirect, reverse, HttpResponse, redirect
from django.utils import timezone
from ghost_post.models import BoastandRoast
from ghost_post.forms import PostForm

# with assistance from Zach
def upvote(request, id):
    html = "index.html"
    try:
        post = BoastandRoast.objects.get(id=id)
    except BoastandRoast.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))
    post.total += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))
    # have the url tell where to go 


def downvote(request, id):
    html = "index.html"
    try:
        post = BoastandRoast.objects.get(id=id)
    except BoastandRoast.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))
    post.total -= 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))
    # have the url tell where to go 


def index(request):
    html = "index.html"
    
    data = BoastandRoast.objects.all().order_by("-date")

    return render(request, html, { "data": data })
    
def boasts_view(request):
    html = "index.html"
    data = BoastandRoast.objects.filter(boast=True).order_by('-date')
    return render(request, html, {"data": data})
    

def roasts_view(request):
    html = "index.html"
    data = BoastandRoast.objects.filter(boast=False)
    return render(request, html, {"data": data})
    




def addpost(request):
    html = "post.html"
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    return render(request, html, {"form": form})


def lovely_view(request):
    html = "index.html"
    data = BoastandRoast.objects.all().order_by("-total")
    return render(request, html, {'data': data})

def hated_view(request):
    html = "index.html"
    data = BoastandRoast.objects.all().order_by("total")
    return render(request, html, {'data': data})




