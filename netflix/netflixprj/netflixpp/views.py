from distutils.log import error
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileFormCreate, ProfileFormDelete
from .models import Profile, Movie


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


method_decorator(login_required, name='dispatch')


class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        form = ProfileFormCreate()
        context = {
            'form': form
        }
        return render(request, 'profilecreate.html', context)

    def post(self, request, *args, **kwargs):
        form = ProfileFormCreate(request.POST or None)
        profiles = request.user.profiles.all()
        if form.is_valid():
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect('netflixpp:profile-list')
        context = {
            'form': form
        }
        return render(request, 'profilecreate.html', context)


method_decorator(login_required, name='dispatch')


class ProfileDelete(View):
    def get(self, request, *args, **kwargs):
        form = ProfileFormDelete()
        context = {
            'form': form
        }
        return render(request, 'profiledelete.html', context)

    def post(self, request, *args, **kwargs):
        form = ProfileFormDelete(request.POST or None)
        if form.is_valid():
            if Profile.objects.filter(**form.cleaned_data).exists():
                instance = Profile.objects.get(**form.cleaned_data)
                instance.delete()
                return redirect('netflixpp:profile-list')
        context = {
            'form': form
        }
        return render(request, 'profiledelete.html', context)


method_decorator(login_required, name='dispatch')


class MovieList(View):
    def get(self, request, profile_id, *args, **kwargs):
        try:
            profile = Profile.objects.get(uuid=profile_id)
            movies = Movie.objects.filter(age_limit=profile.age_limit)
            if profile not in request.user.profiles.all():
                return redirect('netflixpp:profile-list')

            context = {
                'movies': movies
            }

            return render(request, 'movielist.html', context)
        except Profile.DoesNotExist:
            return redirect('netflixpp:profile-list')


method_decorator(login_required, name='dispatch')


class MovieDetail(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)

            context = {
                'movie': movie
            }

            return render(request, 'moviedetail.html', context)
        except Movie.DoesNotExist:
            return redirect('netflixpp:profile-list')
