from user.models import User
from home.error import DoesNotLoginError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_login_user(request):
    user = None
    try :
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
    except KeyError,User.DoesNotExist:
        pass
    return user

def get_common_data(request):
    data = {}
    user = get_login_user(request)
    if not user :
        raise DoesNotLoginError
    fan_num = User.objects.filter(focusUsers=user).count()
    focus_num = user.focusUsers.count()
    data['curr_user']=user
    data['fan_num']=fan_num
    data['focus_num']=focus_num
    return data

def get_pager_data(request,list,data,size):
    try :
        page = int(request.GET['page'])
    except StandardError :
        page = 1
    data_list = list
    paginator = Paginator(data_list, size)
    total_page = paginator.num_pages
    total = paginator.count
    try:
        data_list = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        data_list = paginator.page(page)
    except EmptyPage:
        page = total_page
        data_list = paginator.page(page)

    data['list']=data_list
    data['total']=total
    data['total_page'] = total_page
    start = page -2
    end = page + 2;
    if start < 0 :
        start = 1
        end = 5
    if end > total_page :
        end = total_page
        start = end - 4
        if start < 1:
            start = 1
    pages = range(start,end+1,1)
    data['pages']=pages
    data['page']=page
    return data_list
