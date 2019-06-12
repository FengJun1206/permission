from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from app import models
from app.my_primission.permissions import check_permission
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
@check_permission
def staff_detail(request):
    """员工个人信息"""
    user_obj = models.UserProfile.objects.all()

    return render(request, 'staff_detail.html', {'user_obj': user_obj})

@login_required
@check_permission
def fina_state(request):
    """员工个人信息"""


    return render(request, 'fina_state.html')





def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('.................')
        print(name, email, password)

        models.UserProfile.objects.create_user(name=name, email=email, password=password)
        return redirect('login')
    return render(request, 'signup.html')


def acc_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        # 用户认证，验证用户名、密码是否正确，并返回一个 user 对象
        user_obj = authenticate(email=email, password=password)

        if user_obj:
            print('验证通过...')

            # 将验证成功的用户封装到 request.user 对象中
            login(request, user_obj)       # 在后台为登录用户生成 `session` 数据

            return redirect('/app/')
        else:
            return redirect('login')

    return render(request, 'login.html')


def acc_logout(request):
    auth.logout(request)

    # 注销后重定向到登录页面
    return redirect('login')
