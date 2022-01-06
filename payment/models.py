from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    address1 = models.TextField(max_length=200, blank=True, null=True)
    address2 = models.TextField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=15, blank=True, null=True)
    phone_number = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s billing address"

    def is_fully_filled(self):
        field_names = [f.name for f in self._meta.get_fields()]
        for field_name in field_names:
            value = getattr(self, field_name)
            if value is None or value == '':
                return False
        return True