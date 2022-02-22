from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, FormView
from .forms import RegistForm, UserLoginForm
#passwordが正しいものなのかチェックする
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

#ホーム画面
class HomeView(TemplateView):
    template_name = 'home.html'

#ユーザー登録するView
class RegistUserView(CreateView):
    template_name = 'regist.html'
    #form指定
    form_class = RegistForm  #accounts forms.py内に作成して、import


#ログイン画面
class UserLoginView(FormView):
    template_name = 'user_login.html'
    form_class = UserLoginForm

    def post(self, request, *args, **kwargs):
        username = request.POST['username']           #.get('email')
        password = request.POST['password']           #.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
        return render(request, 'home.html', context={'value': username}) #return redirect('accounts:home')

           
class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:user_login')