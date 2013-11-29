from django import template

register = template.Library()

from ..models import Article

@register.inclusion_tag('news/templatetags/article_year_list.html', takes_context=True)
def article_year_list(context):
    """
    Show a list of all the years for which we have (published) articles.
    
    It relies on a variable 'year' being in the context, and being a date (or datetime)
    instance representing the current year on the target page.
    """

    dates_qs = Article.objects.viewable()
    date_list = dates_qs.dates('start', 'year')[::-1]
    context.update({'date_list': date_list})
    return context

