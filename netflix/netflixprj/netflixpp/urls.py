from django.urls import path
from .views import Home, ProfileList, ProfileCreate, ProfileDelete, MovieList,MovieDetail

app_name = 'netflixpp'

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('profiles/', ProfileList.as_view(), name="profile-list"),
    path('profiles/create/', ProfileCreate.as_view(), name="profile-create"),
    path('profiles/delete/', ProfileDelete.as_view(), name="profile-delete"),
    path('watch/<str:profile_id>/', MovieList.as_view(), name="movie-list"),
    path('watch/detail/<str:movie_id>/',
         MovieDetail.as_view(), name="movie-detail"),
]
