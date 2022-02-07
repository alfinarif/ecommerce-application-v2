from django import template

from notification.models import UserObj, Notification

register = template.Library()

@register.filter
def notifications(user):
    if user.is_authenticated:
        user_obj = UserObj.objects.get(user=user)
        notification = Notification.objects.filter(userobj=user_obj, is_read=False).order_by('-id')
        if notification.exists():
            return notification
        else:
            return None
    else:
        return None


@register.filter
def notification_count(user):
    if user.is_authenticated:
        user_obj = UserObj.objects.get(user=user)
        notification = Notification.objects.filter(userobj=user_obj, is_read=False)
        if notification.exists():
            return notification.count()
        else:
            return 0
    else:
        return 0

          