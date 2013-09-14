from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from user.models import User
from datetime import datetime

def index(request):
    user_id = None
    try :
        user_id = request.session['user_id']
    except KeyError:
        pass
    params = {}
    if user_id :
        try:
            user = User.objects.get(id=user_id)
            params['curr_user'] = user
        except User.DoesNotExist:
            pass
    context = RequestContext(request, params)
    return render(request, 'index.html', context)

def login(request):
    try :
        username = request.POST['username']
        password = request.POST['password']
    except KeyError:
        return HttpResponseRedirect(reverse('home:signin', args=()))
    success = True
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist :
        success = False
    if success and password != user.password :
        success = False
    if not success :
        context = RequestContext(request, {'error':'true'})
        return render(request, 'home/login.html', context)
        #return HttpResponseRedirect(reverse('home:signin', args=()))
    request.session['user_id']=user.id
    return HttpResponseRedirect(reverse('index', args=()))

def logout(request):
    context = RequestContext(request, {})
    request.session['user_id'] = None
    return render(request, 'index.html', context)

def register(request):
    context = RequestContext(request, {})
    return render(request, 'home/register.html', context)

def signin(request):
    context = RequestContext(request, {})
    return render(request, 'home/login.html', context)

def save(request):
    user=User()
    user.username=request.POST['username']
    user.nickname=request.POST['nickname']
    user.password=request.POST['password']
    user.lastLoginTime=datetime.today()
    user.registerTime=datetime.today()
    user.logo='static/image/logo.jpg'
    user.save()
    request.session['user_id']=user.id
    return HttpResponseRedirect(reverse('index', args=()))

def check(request,user_name):
    response = HttpResponse()
    users=[]
    try:
        users = User.objects.get(username=user_name)
        num = 1
    except User.DoesNotExist:
        num = 0
    response.write(num)
    return response

def profile(request,user_name):
    pass



