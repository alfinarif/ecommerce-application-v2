from django.contrib import admin
from django.dispatch.dispatcher import NO_RECEIVERS

from notification.models import Notification


admin.site.register(Notification)
