from django import template
from chess.models import Articles

register = template.Library()


@register.simple_tag()
def get_articles(count=5):
    return Articles.objects.order_by("-id")[:count]