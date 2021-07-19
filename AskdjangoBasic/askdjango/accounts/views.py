from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required #로그인 안 한 사람은 settings의 login으로 이동하게 해준다.
def profile(request):
    return render(request, 'accounts/profile.html')
