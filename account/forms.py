from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from account.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')
        exclude = ('user', )


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
