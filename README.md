# master-project

this is a News APi with django REST framework 

for news data it screpe Hacker news ***RSS feed***

or it can scrape any news site with a ***RSS feed***

async in handeld with <b>Celery</b>

## How does it work ? 


with this command you can *__scrape th Hacker news__*

    python manage.py scrape

and with *__scrapebylink__* you can scrape any news site with a RSS feed

    python manage.py scrapebylink

data after being scraped will be saved in psql database

news is accessible via /api/news/

Users can search in news list in fields [title or source]

## Accounts 

users can be registerd in /api/accounts/register/

**every time a user registers** a **token will be created for the new user using signals**

and **JWT** token is supported as well 

users can change password too
