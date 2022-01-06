from django import template

from store.models import MyLogo, MyFavicon


register = template.Library()


@register.filter
def logo(request):
    if request:
        logo = MyLogo.objects.filter(is_active=True).order_by('-id').first()
        return logo.image.url

    else:
        logo = MyLogo.objects.filter(is_active=True).order_by('-id').first()
        return logo.image.url

@register.filter
def favicon(user):
    if user.is_authenticated:
        logo = MyFavicon.objects.filter(user = user, is_active=True).order_by('-id').first()
        return logo.image.url