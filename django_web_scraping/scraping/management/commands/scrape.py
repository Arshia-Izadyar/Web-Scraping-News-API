from bs4 import BeautifulSoup
import requests
from requests.exceptions import Timeout, TooManyRedirects, ConnectionError
from datetime import datetime
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'this command will scrape news from hacker news'

    def handle(self, *args, **options):
        print('starting scrap .... ')
        art_list = list()
        try:

            r = requests.get('https://news.ycombinator.com/rss')
            soup = BeautifulSoup(r.content, 'lxml')
            art = soup.find_all('item')
            date_format = "%a, %d %b %Y %H:%M:%S %z"
            # datetime_list = []

            for i in art:
                title = i.find('title').string
                link = i.find('link').string
                pub_date = i.find('pubdate').string
                published = datetime.strptime(pub_date, date_format)
                # datetime_list.append(datetime.strptime(pub_date, date_format))
                article = {
                    'title': title,
                    'link': link,
                    'published': published,
                    'source': 'HackerNews RSS'
                }
                art_list.append(article)

            print('finished scrape')

            return 'ok'
        except (Timeout, TooManyRedirects, ConnectionError) as e:
            print('the scrape Failed error ::', e)
