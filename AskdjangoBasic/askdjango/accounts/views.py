from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from .forms import SignupForm

# 함수 기반
# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect(settings.LOGIN_URL)
#     else:
#         form = SignupForm()
#     return render(request, 'accounts/signup.html', {
#         'form': form,
#     })

# 클래스 기반
signup = CreateView.as_view(model=User, 
        form_class=SignupForm,
        success_url=settings.LOGIN_URL,
        template_name='accounts/signup.html')

@login_required #로그인 안 한 사람은 settings의 login으로 이동하게 해준다.
def profile(request):
    return render(request, 'accounts/profile.html')
