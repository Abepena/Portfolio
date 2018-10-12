from django import template
from django.utils.safestring import mark_safe
import markdown2


register = template.Library()

@register.filter
def markdown_to_html(markdown_text):
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)