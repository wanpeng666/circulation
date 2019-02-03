from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from apps.users.models import Users


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username', '')
        pwd = request.POST.get('password', '')
        email = request.POST.get('email', '')
        if not all([username, pwd, email]):
            content = {
                'success': False,
                'message': '请把信息填写完整',
            }
            return JsonResponse(content)
        try:
            user = Users.objects.create_user(username=username, password=pwd, email=email)
        except Exception as e:
            content = {
                'success': False,
                'message': '用户创建失败',
            }
            return JsonResponse(content)
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'index.html', user)


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'message': ''})

    def post(self, request):
        username = request.POST.get('username', '')
        pwd = request.POST.get('pwd', '')
        user = authenticate(username=username, password=pwd)
        if user:
            login(request, user)
            # content = {
            #     'success': True,
            #     'message': '登录成功',
            # }
            return redirect(reverse('mast:incidents'))
        else:
            return render(request, 'login.html', {'message': '登录失败'})
