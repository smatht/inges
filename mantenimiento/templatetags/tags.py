from django import template

register = template.Library()

@register.simple_tag
def blog_url():
    return 'https://medium.com/@sisinges/'