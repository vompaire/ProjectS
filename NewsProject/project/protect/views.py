from django.contrib.auth import authenticate, login
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User


class LoginAjaxView(View):
    def post(self,request):
        email= request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user=authenticate(email=email, password=password)
            if user:
                login(request,user)
                return JsonResponse(data={}, status=201)
            return JsonResponse(
                data={'error':"хуева"},
                status=400
            )
        return JsonResponse(
            data={'error':'введите логин и пароль'},
            status=400
        )


class RegistAjaxView(View):
    def post(self, request):
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password and nickname:

            try:
                user = User.objects.create_user(username=nickname, email=email, password=password)
                if user:
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    return JsonResponse(data={}, status=201)
            except Exception as e:
                return JsonResponse(
                    data={'error': "хуева" + str(e)},
                    status=400
                )
        return JsonResponse(
            data={'error': 'введите логин и пароль и имя'},
            status=400
        )


class ResetAjaxView(View):
    def post(self, request):
        email = request.POST.get('email')
        if email:
            return JsonResponse(data={}, status=201)
        return JsonResponse(
            data={'error': 'введите логин и пароль'},
            status=400
        )