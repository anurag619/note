from notes.models import Note
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from notes.forms import NoteForm

def home(request):
    
    return render(request, "notes/home.html")
    

def about(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, 'notes/about.html')

def all_notes(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect(settings.LOGIN_URL)
    return render_to_response('notes/all_notes.html',{'notes': Note.objects.all()})


def get_notes(request,note_id=1):
    return render_to_response('notes/get_notes.html',{'note': Note.objects.get(id=note_id)})


def create(request):
    if request.POST:
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            
            url = reverse(all_notes)
            return HttpResponseRedirect(url)
    else:
        form = NoteForm() 
    args={}
    args.update(csrf(request))
    args['form']= form

    return render_to_response('notes/create.html', args) 

