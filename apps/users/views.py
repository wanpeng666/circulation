from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from apps.users.models import User


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
            user = User.objects.create_user(username=username, password=pwd, email=email)
        except Exception as e:
            content = {
                'success': False,
                'message': '用户创建失败',
            }
            return JsonResponse(content)
        login(request, user)