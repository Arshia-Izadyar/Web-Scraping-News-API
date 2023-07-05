from django.core.management.base import BaseCommand, CommandParser
from bs4 import BeautifulSoup
import requests
from requests.exceptions import Timeout, TooManyRedirects, ConnectionError, ProxyError
from datetime import datetime
from django.core.management.base import BaseCommand

from scraping.utils import save_function


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("arg1", type=str, help="enter your rss feed link")

    def handle(self, *args, **options):
        link = options["arg1"]
        arti_list = []
        self.stdout.write("Startin th Scrape ...")
        try:
            r = requests.get(link)
            soup = BeautifulSoup(r.content, features="xml")
            art = soup.find_all("item")
            for i in art:
                title = i.find("title").string
                links = i.find("link").string
                article = {
                    "title": title,
                    "link": links,
                    "published": datetime.now(),
                    "source": link,
                }
                arti_list.append(article)
            self.stdout.write("Finished Scrape .")
            return save_function(arti_list)
        except (Timeout, TooManyRedirects, ConnectionError, ProxyError) as e:
            return self.stdout.write("Can't complete the scrape Error: ", e)
