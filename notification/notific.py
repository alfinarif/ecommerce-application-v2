from notification.models import UserObj, Notification

class SendNotification:
    def __init__(self, user, message) -> None:
        self.user = user
        self.message = message

        user_obj = UserObj.objects.get(user=self.user)
        notification = Notification.objects.create(message=self.message, is_read=False)
        notification.userobj.add(user_obj)
        notification.save()