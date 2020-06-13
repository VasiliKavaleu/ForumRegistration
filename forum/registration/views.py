from django.shortcuts import render
from django.http import HttpResponse
from registration.models import Participants, Good
from .forms import PostForm
from django.shortcuts import redirect

def registration(request):
    if request.method == 'POST':
        form = PostForm(request.POST) 
        if form.is_valid():
            participant = form.save()
            participant.save()
            return render(request, 'success.html')
    else:
        form = PostForm()
    return render(request, 'registration.html', {'form': form})
