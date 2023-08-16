from datetime import datetime, timedelta
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import New  # Замените .models на ваш путь к модели New
from .forms import NewForm  # Замените .forms на ваш путь к форме NewForm
from .filters import NewFilter  # Замените .filters на ваш путь к фильтру NewFilter
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from allauth.account.forms import SignupForm
from django.contrib.auth import logout
import requests
import scrapy
from bs4 import BeautifulSoup
from .models import NewsOut
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from telethon.sync import TelegramClient
from django.http import JsonResponse
from django.shortcuts import render
import asyncio
import concurrent.futures
import asgiref
from aiohttp import ClientSession
from telethon.sync import TelegramClient


async def get_telegram_messages(api_id, api_hash):
    # Создаем сессию для работы с HTTP
    async with ClientSession() as session:
        # Создаем клиент Telegram
        async with TelegramClient('session_name', api_id, api_hash, loop=session.loop) as client:
            # Имя пользователя или канала, из которого мы хотим получить сообщения
            channel_username = 'dtfbest'
            # Получаем сущность (чат или канал)
            entity = await client.get_entity(channel_username)
            # Максимальное количество сообщений для получения
            message_limit = 10
            # Получаем сообщения из чата или канала
            all_mes = await client.get_messages(entity, limit=message_limit)
            # Формируем список словарей с информацией о каждом сообщении
            messages = []
            for mes in all_mes:
                message_info = {
                    'text': mes.text,
                    'date': mes.date,
                    'media': None
                }
                # Если у сообщения есть медиа, добавляем информацию о медиа-файле
                if mes.media:
                    if mes.photo:
                        media_type = 'photo'
                        media = await mes.download_media()
                    elif mes.document:
                        media_type = 'document'
                        media = await mes.download_media()
                    elif mes.video:
                        media_type = 'video'
                        media = await mes.download_media()
                    # Можете добавить другие типы медиа (аудио и т.д.) по аналогии
                    else:
                        media_type = None
                        media = None
                    message_info['media'] = {
                        'type': media_type,
                        'data': media
                    }
                messages.append(message_info)
            messages = [{'text': mes.text, 'photo_path': f'/media/photo_{mes.id}.jpg' if mes.media and mes.photo else None} for mes in all_mes]
            return render(request, 'telega.html', {'messages': messages})



# Обработчик представления (view) для страницы telega.html
def telega(request):
    # Ваши API ID и API Hash для Telegram
    api_id = 21349304
    api_hash = 'b2f97a207e389c38e75c57627c5698f1'

    # Создаем новый цикл событий asyncio
    loop = asyncio.new_event_loop()
    # Устанавливаем этот цикл событий как текущий
    asyncio.set_event_loop(loop)

    # Создаем пул потоков для выполнения асинхронных функций
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Запускаем асинхронную функцию get_telegram_messages
        # и ожидаем результат с использованием нового цикла событий
        messages = loop.run_until_complete(get_telegram_messages(api_id, api_hash))

    # Возвращаем результат рендеринга шаблона telega.html
    # и передаем список сообщений в качестве контекста для шаблона
    return render(request, 'telega.html', {'messages': messages})


def scrape_cybersport_news():
    print("Scraping cybersport news...")

    url = 'https://www.cybersport.ru/?sort=-publishedAt'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for article in soup.find_all('div', class_='rounded-block root_d51Rr with-hover no-padding no-margin'):
        site = url
        title = article.find('h3', class_='title_nSS03').text.strip()
        link = 'https://www.cybersport.ru' + article.find('a', class_='link_CocWY')['href']
        image_element = article.find('div', class_='image_f4Qfq')

        date_time_with_timezone = article.find('time', class_='pub_AKjdn')['datetime']

        dt_object = datetime.strptime(date_time_with_timezone, "%Y-%m-%dT%H:%M:%S%z")

        date_time_parts = dt_object - dt_object.utcoffset()
        data_public_from_site = date_time_parts.strftime("%Y-%m-%dT%H:%M:%S")

        if image_element:
            image = image_element.find('img')['src']
        else:
            image = ""

        news, created = NewsOut.objects.get_or_create(title=title, defaults={'link': link, 'image': image, 'site': site, 'data_public_from_site': data_public_from_site})

    print("News(cybersport) scraped and saved to the database.")


def scrape_gamemag_news():
    print("Scraping gamemaga news")

    url = 'https://gamemag.ru'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for article in soup.select('div[class="news-item"]'):
        site = url
        title = article.find('a', class_='news-item__text').text.strip()

        link_element = article.find('a', class_='news-item__link')['href']

        image_element = article.find('img', class_="news-item__img")
        link = url + link_element
        if image_element and 'src' in image_element.attrs:
            image = url + image_element['src']

        else:
            image = None
        date_time_with_timezone = article.find('span', class_='news-item__hashtag').text.strip()
        time_obj = datetime.strptime(date_time_with_timezone, '%d.%m.%Y %H:%M') - timedelta(hours=3)

        data_public_from_site = time_obj.strftime('%Y-%m-%dT%H:%M:%S')
        #
        # dt_object = datetime.strptime(date_time_with_timezone, "%d.%m.%Y %H:%M")
        #
        # date_time_parts = dt_object - dt_object.utcoffset()
        # data_public_from_site = date_time_parts.strftime("%Y-%m-%dT%H:%M:%S")
        news, created = NewsOut.objects.get_or_create(title=title, defaults={'link': link, 'image': image, 'site': site, 'data_public_from_site': data_public_from_site})

    #   print(link, '111', site, '222', title, '333', image, '444', data_public_from_site, )
    print("News(gamemag) scraped and saved to the database.")
    #     news_list.append(news)
    # return render(request, 'news_list.html', {'news_list': news_list})


class NewsOutView(ListView):
    model = NewsOut
    template_name = 'news.html'
    context_object_name = 'newsout'
    paginate_by = 10
    ordering = '-data_public_from_site'


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
    template_name = 'New_edit.html'


class NewEdit(UpdateView):
    form_class = NewForm
    model = New
    template_name = 'new_edit.html'


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
