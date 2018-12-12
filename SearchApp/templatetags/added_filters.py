from django.template import Library
from django.utils.safestring import mark_safe
import json

register = Library()

@register.filter(is_safe=True)
def get_in_js(obj):
	return mark_safe(json.dumps(obj))