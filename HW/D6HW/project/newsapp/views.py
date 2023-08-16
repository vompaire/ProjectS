from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import New


class NewsList(ListView):

    model = New

    ordering = '-data_public'

    template_name = 'news.html'

    context_object_name = 'news'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['time_now'] = datetime.utcnow()

        context['next_sale'] = None
        return context


class NewDetail(DetailView):

    model = New

    template_name = 'new.html'

    context_object_name = 'news'
