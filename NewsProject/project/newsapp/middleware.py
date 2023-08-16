from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from newsapp.views import scrape_cybersport_news, scrape_gamemag_news


class BackgroundSchedulerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        start_scheduler()  # Запуск планировщика

    def __call__(self, request):
        response = self.get_response(request)
        return response

def start_scheduler():
    scheduler = BackgroundScheduler()

    scheduler.add_job(scrape_gamemag_news)
    scheduler.add_job(scrape_gamemag_news, 'interval', minutes=10)
    scheduler.add_job(scrape_cybersport_news)
    scheduler.add_job(scrape_cybersport_news, 'interval', minutes=10)
    scheduler.start()
