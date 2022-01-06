from django import forms


class CouponCodeForm(forms.Form):
    code = forms.CharField()