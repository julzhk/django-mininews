from mininews.views import MininewsArchiveIndexView, MininewsYearArchiveView, \
    MininewsDetailView

from .models import Article


class ArticleArchiveView(MininewsArchiveIndexView):
    model = Article
    context_object_name = 'article_list'


class ArticleYearArchiveView(MininewsYearArchiveView):
    model = Article
    context_object_name = 'article_list'
    date_list_period = 'year'

    def get_context_data(self, **kwargs):
        """Not strictly required for the demo - I just prefer for the 'year' view to show
        a sidebar with *all* the years that have articles."""

        context = super(ArticleYearArchiveView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated() and self.request.user.is_staff:
            qs = self.model.objects.all()
        else:
            qs = self.model.objects.live()
        context['date_list'] = qs.dates('start', 'year', order='DESC')
        return context


class ArticleDetailView(MininewsDetailView):
    model = Article
    context_object_name = 'article'
