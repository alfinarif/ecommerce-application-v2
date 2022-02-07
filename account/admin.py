from django.contrib import admin
from account.models import Profile, User

admin.site.register(User)
admin.site.register(Profile)
