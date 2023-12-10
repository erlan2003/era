from django.shortcuts import render, redirect, get_object_or_404
from .models import Attraction, Comment
from .forms import AttractionForms
from django.views.generic import DetailView
from .forms import CommentForms
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

class CommentDetailView(DetailView):
    model = Attraction
    template_name = 'main/add_comment.html'
    context_object_name = 'attraction'


class AttractionDetailView(DetailView):
    model = Attraction
    template_name = 'main/details_view.html'
    context_object_name = 'attraction'


def add_comment(request, attraction_id):
    error = ''
    attraction = Attraction.objects.get(pk=attraction_id)
    if request.method == "POST":
        form = CommentForms(request.POST)
        if form.is_valid():
            #form.user = request.user  # устанавливаем текущего пользовател
            form.save()
            detail_url = reverse('attraction-detail', kwargs={'pk': attraction.id})
            return redirect(detail_url)
        else:
            error = 'Форма была неверной!'

    form = CommentForms()
    data = {
        'form': form,
        'error': error,
        'attraction': attraction,
    }
    return render(request, 'main/add_comment.html', data)

def index(request):
    attractions = Attraction.objects.all()
    return render(request, 'main/index.html', {'attractions': attractions})
def about(request):
    return render(request, 'main/about.html')
def add_attraction(request):
    error = ''
    if request.method == "POST":
        form = AttractionForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной!'

    form = AttractionForms()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_attraction.html', data)
def tours(request):
    return render(request, 'main/tours.html')
def cooperation(request):
    return render(request, 'main/cooperation.html')

def unpublish_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, 'Комментарий успешно удален.')
    return redirect(request.META['HTTP_REFERER'])

@login_required
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})