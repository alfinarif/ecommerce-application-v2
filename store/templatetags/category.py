from django import template
from store.models import Category

register = template.Library()


@register.filter
def category(user):
    if user.is_authenticated:
        cat = Category.objects.filter(parent=None)
        return cat