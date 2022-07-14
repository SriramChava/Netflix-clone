from django.urls import path
from .views import Home

app_name = 'netflixpp'

urlpatterns = [
    path('', Home, name='home')
]
