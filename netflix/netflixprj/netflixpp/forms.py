from django.forms import ModelForm
from netflixpp.models import Profile


class ProfileFormCreate(ModelForm):
    class Meta:
        model = Profile
        exclude = ['uuid']


class ProfileFormDelete(ModelForm):
    class Meta:
        model = Profile
        exclude = ['uuid', 'age_limit']
