from django import template
from climbcast.models import CraggArea

register = template.Library()

@register.inclusion_tag('climbcast/craggarea_sidebar.html')
def get_craggarea_list(cragg=None):
    return {'craggareas': CraggArea.objects.all(), 'act_cragg': cragg}
