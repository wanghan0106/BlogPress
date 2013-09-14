from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from user.models import User
from blog.models import Column,Article
from home.error import DoesNotLoginError
from user import *

import os

def profile(request):
    try :
        data = get_common_data(request)
    except DoesNotLoginError:
        return HttpResponseRedirect(reverse('index', args=()))
    user = data['curr_user']
    data['profile_menu']=1
    data['is_profile']=1
    context = RequestContext(request, data)
    return render(request, 'user/profile/profile.html', context)

def save_profile(request):
    user = get_login_user(request)
    if not user :
        return HttpResponseRedirect(reverse('index', args=()))
    user.desc = request.POST['desc'].strip()
    user.favorite = request.POST['favorite'].strip()
    user.save()
    return HttpResponseRedirect(reverse('user:profile', args=()))

def logo(request):
    try :
        data = get_common_data(request)
    except DoesNotLoginError:
        return HttpResponseRedirect(reverse('index', args=()))
    data['profile_menu']=1
    data['is_logo']=1
    context = RequestContext(request, data)
    return render(request, 'user/profile/change_logo.html', context)

def save_logo(request):
    user = get_login_user(request)
    if not user :
        return HttpResponseRedirect(reverse('index', args=()))
    try :
        logoFile = request.FILES['logoFile']
        dir = settings.STATICFILES_DIRS[0]
        dir = "%s/image/logo" % dir #% (dir,user.id%1000,user.id)
        user_or_make_dir(dir)
        dir = "%s/%d" % (dir,user.id%1000)
        user_or_make_dir(dir)
        dir = "%s/%d" % (dir,user.id)
        user_or_make_dir(dir)
        file_name = 'logo%s' % logoFile.name[logoFile.name.index("."):]
        path = "%s/%s" % (dir,file_name)
        with open(path, 'wb+') as dest:
            for chunk in logoFile.chunks():
                dest.write(chunk)
            dest.flush()
            dest.close()
        user.logo = 'static/image/logo/%d/%d/%s' % (user.id%1000,user.id,file_name)
        user.save()
    except KeyError,StandardError :
        pass
    return HttpResponseRedirect(reverse('user:logo', args=()))

def user_or_make_dir(dir) :
    if not os.path.isdir(dir) :
        os.mkdir(dir)

def password(request):
    try :
        data = get_common_data(request)
    except DoesNotLoginError:
        return HttpResponseRedirect(reverse('index', args=()))
    data['profile_menu']=1
    data['is_password']=1
    context = RequestContext(request, data)
    return render(request, 'user/profile/change_password.html', context)

def check_password(request,password):
    response = HttpResponse()
    result = 0
    user = get_login_user(request)
    if not user :
        pass
    if password != user.password :
        result = 1
    response.write(result)
    return response

def save_password(request):
    user = get_login_user(request)
    if not user :
        return HttpResponseRedirect(reverse('index', args=()))
    user.password = request.POST['password']
    user.save()
    return HttpResponseRedirect(reverse('user:password', args=()))

def blog(request):
    try :
        data = get_common_data(request)
    except DoesNotLoginError:
        return HttpResponseRedirect(reverse('index', args=()))
    get_pager_data(request,Article.objects.all(),data,5)
    data['blog_menu']=1
    data['is_blog']=1
    context = RequestContext(request, data)
    return render(request, 'user/blog/blog.html', context)


def column(request):
    try :
        data = get_common_data(request)
    except DoesNotLoginError:
        return HttpResponseRedirect(reverse('index', args=()))
    get_pager_data(request,Column.objects.all(),data,5)
    data['blog_menu']=1
    data['is_column']=1
    context = RequestContext(request, data)
    return render(request, 'user/blog/column/column.html', context)

def add_blog(request):
    try :
        data = get_common_data(request)
    except DoesNotLoginError:
        return HttpResponseRedirect(reverse('index', args=()))
    data['blog_menu']=1
    data['is_blog']=1

    context = RequestContext(request, data)
    return render(request, 'user/blog/detail.html', context)

def save_blog(request):
    return HttpResponseRedirect(reverse('user:blog', args=()))

def delete_blog(request,blog_id):
    return HttpResponseRedirect(reverse('user:blog', args=()))

def add_column(request):
    try :
        data = get_common_data(request)
    except DoesNotLoginError:
        return HttpResponseRedirect(reverse('index', args=()))
    data['blog_menu']=1
    data['is_column']=1
    context = RequestContext(request, data)
    return render(request, 'user/blog/column/detail.html', context)

def edit_column(request,column_id):
    try :
        data = get_common_data(request)
    except DoesNotLoginError:
        return HttpResponseRedirect(reverse('index', args=()))
    data['blog_menu']=1
    data['is_column']=1
    try :
        column = Column.objects.get(id=column_id)
        data['column'] = column
    except Column.DoesNotExist :
        pass
    context = RequestContext(request, data)
    return render(request, 'user/blog/column/detail.html', context)

def save_column(request):
    user = get_login_user(request)
    if not user :
        return HttpResponseRedirect(reverse('index', args=()))
    try :
        column_id = request.POST['id']
        column = Column.objects.get(id=column_id)
    except StandardError:
        column = Column()
        column.articlenum = 0
        column.owner = user
    column.name = request.POST['name']
    column.save()
    return HttpResponseRedirect(reverse('user:column', args=()))

def delete_column(request,column_id):
    try :
        column = Column.objects.get(id=column_id)
        column.delete()
    except Column.DoesNotExist :
        pass
    return HttpResponseRedirect(reverse('user:column', args=()))

def focus(request):
    pass
