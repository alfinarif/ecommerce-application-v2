from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from notification.models import UserObj, Notification


def seenNotification(request, pk):
    if request.user.is_authenticated:
        user_obj = UserObj.objects.get(user=request.user)
        notification_qs = Notification.objects.get(id=pk)
        notification_qs.userobj.remove(user_obj)
        notification_qs.is_read = True
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('account:login')
