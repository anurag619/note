from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegisterForm

def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('note/login.html', c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid') 

def loggedin(request):
    return render_to_response('note/loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('note/invalid.html')

def logout(request):
    auth.logout(request)
    return render_to_response('note/logout.html')


def register(request):
    if request.method =='POST':
        form = MyRegisterForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/accounts/success')
    args = {}
    args.update(csrf(request))
    
    args['form']=MyRegisterForm()
    
    return render_to_response('note/register.html', args)

def success(request):
    return render_to_response('note/success.html')



