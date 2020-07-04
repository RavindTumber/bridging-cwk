from django import template
from math import ceil

register = template.Library()

@register.filter
def read_time(wordcount):
    """Calculates the average reading time for a blog post."""
    avg_reading_speed = 200
    return ceil(wordcount/avg_reading_speed)