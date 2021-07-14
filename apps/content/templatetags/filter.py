from math import ceil

from django import template

register = template.Library()


@register.filter
def mod(num, val):
    return num % val


@register.filter
def split_to_3_columns(queryset):
    values = list(queryset.all())
    split = int(ceil(len(values) / 3.))
    columns = [values[i * split:(i + 1) * split] for i in range(3)]
    print(columns)
    return columns
