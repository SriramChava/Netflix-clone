from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('netflixpp:profile-list')
        return render(request, 'index.html')


method_decorator(login_required, name='dispatch')


class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()
        context = {
            'profiles': profiles
        }
        return render(request, 'profilelist.html', context)
