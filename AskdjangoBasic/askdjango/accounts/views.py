from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import redirect, render, resolve_url
from .forms import SignupForm

# 함수 기반
# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)#로그인 처리
#             next_url = request.GET.get('next') or 'profile' #로그인 하면 어느 페이지로 넘어갈지 정한다. 
#             return redirect(next_url)
#     else:
#         form = SignupForm()
#     return render(request, 'accounts/signup.html', {
#         'form': form,
#     })


# 클래스 기반
class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next') or 'profile'
        return resolve_url(next_url)#resolve_url
    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())

signup = SignupView.as_view()

@login_required #로그인 안 한 사람은 settings의 login으로 이동하게 해준다.
def profile(request):
    return render(request, 'accounts/profile.html')
