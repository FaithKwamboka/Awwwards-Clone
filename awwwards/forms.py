from django import forms
from django.contrib.auth.models import User
from .models import * 
from pyuploadcare.dj.forms import ImageField


class PostForm(forms.ModelForm):
    photo = ImageField(label='')

    class Meta:
        model = Post
        fields = ('photo', 'title', 'url', 'description', 'technologies',)


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    # profile_picture = ImageField(label='')
    class Meta:
        model = Profile
        fields = ['name', 'location', 'profile_picture', 'bio', 'email']


class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']