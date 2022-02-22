from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password


#4つのフィールド作成 このフォームを使用してユーザー登録を行う
class RegistForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    age = forms.IntegerField(label='年齢', min_value=0)
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())


    class Meta:
        model = Users
        fields = ['username', 'age', 'email', 'password']

    def save(self, commit=False):
        user = super().save(commit=False)
        #パスワードが適切なものか
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

#ログインフォーム
class UserLoginForm(forms.Form):
    username = forms.CharField(label='ユーザー名')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())