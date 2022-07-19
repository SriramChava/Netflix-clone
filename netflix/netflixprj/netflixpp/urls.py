from django.urls import path
from .views import Home, ProfileList, ProfileCreate,ProfileDelete

app_name = 'netflixpp'

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('profiles/', ProfileList.as_view(), name="profile-list"),
    path('profiles/create/', ProfileCreate.as_view(), name = "profile-create"),
    path('profiles/delete/',ProfileDelete.as_view(), name = "profile-delete" )
]
