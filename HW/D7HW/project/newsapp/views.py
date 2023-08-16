from datetime import datetime, timedelta

from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import New
from .filters import NewFilter
from .forms import NewForm





class NewsList(ListView):
    model = New
    ordering = '-data_public'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        return context


class NewDetail(DetailView):
    model = New
    template_name = 'new.html'
    context_object_name = 'new'


class NewCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = NewForm
    # модель товаров
    model = New
    # и новый шаблон, в котором используется форма.
    template_name = 'new_edit.html'


class NewEdit(UpdateView):
    form_class = NewForm
    model = New
    template_name = 'New_edit.html'


class NewDelete(DeleteView):
    model = New
    template_name = 'new_delete.html'
    success_url = reverse_lazy('new_list')

class NewSearch(ListView):
    model = New
    ordering = '-data_public'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now'] = datetime.utcnow()
        return context
