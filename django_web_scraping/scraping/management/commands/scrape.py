from bs4 import BeautifulSoup
# from celery import shared_task
import requests
from requests.exceptions import Timeout, TooManyRedirects, ConnectionError
from datetime import datetime
from django.core.management.base import BaseCommand
from scraping.utils import save_function

class Command(BaseCommand):
    help = "this command will scrape news from hacker news"

    # @shared_task
    def handle(self, *args, **options):
        self.stdout.write("starting scrap .... ")
        art_list = list()
        try:
            r = requests.get("https://news.ycombinator.com/rss")
            soup = BeautifulSoup(r.content, "lxml")
            art = soup.find_all("item")
            date_format = "%a, %d %b %Y %H:%M:%S %z"

            for i in art:
                title = i.find("title").string
                link = i.find("link").next_sibling.strip()
                pub_date = i.find("pubdate").string
                published = datetime.strptime(pub_date, date_format)
                # datetime_list.append(datetime.strptime(pub_date, date_format))
                article = {
                    "title": title,
                    "link": link,
                    "published": published,
                    "source": "HackerNews RSS",
                }
                art_list.append(article)

            self.stdout.write("finished scrape")

            return save_function(art_list)
        except (Timeout, TooManyRedirects, ConnectionError) as e:
            self.stdout.write("the scrape Failed error ::", e)
