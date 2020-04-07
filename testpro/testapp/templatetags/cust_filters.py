from django import template
register=template.Library()
def truncate2(value):
    format=value[0:2]
    return format
register.filter("truncate",truncate2)