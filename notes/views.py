from notes.models import Note
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from forms import RegistrationForm, LoginForm, NoteForm
from django.template import RequestContext
from models import Student, Note


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse(Profile))

    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                   password = form.cleaned_data['password']
            )
            user.save()
            
            return HttpResponseRedirect(reverse(login_user))
        else:
            return render_to_response('index.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('index.html', context, context_instance=RequestContext(request))


@login_required
def Profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse(login_user))
    Student = request.user.get_profile
    context = {'Student': Student}
    return render_to_response('profile.html', context, context_instance=RequestContext(request))


def login_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse(login_user))
    if request.method == 'POST':
        submit = LoginForm(request.POST)
        if submit.is_valid():
            username = submit.cleaned_data['username']
            password = submit.cleaned_data['password']
            student = authenticate(username=username, password=password)
            if student is not None:
                auth.login(request, student)
                return HttpResponseRedirect(reverse(Profile))
            else:
                return HttpResponseRedirect(reverse(invalid_login))
    else:
        submit = LoginForm()
        context = {'submit': submit}
        return render_to_response('login.html',context, context_instance=RequestContext(request))

def invalid_login(request):
   return render_to_response('invalid_login.html')

def logout_user(request):
    logout(request)
    return render_to_response('logout.html',{'user': request.user.username})


@login_required
def create(request):
 #   if not request.user.is_authenticated():
  #      return HttpResponseRedirect(reverse(login))

    if request.method == 'POST':
        note_form = NoteForm(request.POST)
        if note_form.is_valid():
            note_form.save()
            return HttpResponseRedirect('/all_notes')
        #else:
            # Do something in case if form is not valid
            #raise Http404 

    args={}
    args.update(csrf(request))
    args['note_form']= NoteForm()
    return render_to_response('create.html', args) 

@login_required
def edit_note(request,note_id, template_name='edit_note.html'):
    e = get_object_or_404(Note, pk=note_id)
    form = NoteForm(request.POST or None, instance=e)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/all_notes')

    return render(request, template_name, {'form':form})

    #def server_update(request, pk, template_name='servers/server_form.html'):
    #e = Note.objects.get(pk=note_id)
    #form = NoteForm(request.GET, instance=e)
    #if form.is_valid():
        #form.save()
        
@login_required
def all_notes(request, username):
    return render_to_response('edit.html',{'notes': Note.objects.get(username)})


def get_notes(request,note_id=1):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse(login_user))
    return render_to_response('get_notes.html',{'all_note': Note.objects.get(id=note_id)})

def delete(request,note_id, template_name='delete.html'):
    d= get_object_or_404(Note, pk=note_id)    
    if request.method=='POST':
        d.delete()
        return HttpResponseRedirect('/all_notes')
    return render(request, template_name, {'note':d})

