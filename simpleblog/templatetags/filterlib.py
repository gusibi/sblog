from django import template
from django.template.defaultfilters import stringfilter

from django.conf import settings

register = template.Library()

@register.filter(name='markdown')
@stringfilter
def markdown(value, arg=''):
    """
    Filter to create HTML out of Markdown, using custom extensions.

    The diffrence between this filter and the django-internal markdown
    filter (located in ``django/contrib/markup/templatetags/markup.py``)
    is that this filter enables extensions to be load.

    Usage::

        {{ object.text|markdown }}
        {{ object.text|markdown:"save" }}
        {{ object.text|markdown:"codehilite" }}
        {{ object.text|markdown:"save,codehilite" }}

    This code is taken from
    http://www.freewisdom.org/projects/python-markdown/Django
    """
    try:
        import markdown
    except ImportError:
        if settings.DEBUG:
            raise (template.TemplateSyntaxError,
                   "Error in {% markdown %} filter: "
                   + "The markdown library isn't installed.")
        else :
            from django.utils.html import escape, linebreaks
            return linebreaks(escape(value))
    else:
        extensions=arg.split(",")
        if len(extensions) > 0 and extensions[0] == "safe" :
            extensions = extensions[1:]
            safe_mode = True
        else :
            safe_mode = False
        return markdown.markdown(value, extensions, safe_mode=safe_mode)