import config
import feedparser
from database.db import Database
from telegram_bot import bot
import schedule
import time
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)

db = Database(config.DATABASE, config.PGUSER,
              config.PGPASSWORD, config.HOST, config.PORT)


myfeeds = [
    "https://realpython.com/atom.xml",
    'https://www.freecodecamp.org/news/tag/python/rss',
    'https://habr.com/ru/rss/hub/python/',
    'https://habr.com/ru/rss/hub/django/',
    'https://www.reddit.com/r/python/.rss',
    'https://dev.to/feed/tag/python',
    'https://webdevblog.ru/category/python/feed/',
    'https://yasoob.me/index.xml',
    'https://codecamp.ru/blog/rss/',
    'https://python-scripts.com/feed',
    'https://www.blog.pythonlibrary.org/feed/',
    'https://www.codesnail.com/feed/',
    'https://shwanoff.ru/category/programming/python/feed/',
    'https://www.youtube.com/feeds/videos.xml?channel_id=UC9MK8SybZcrHR3CUV4NMy2g',
    'https://www.youtube.com/feeds/videos.xml?channel_id=UCBGENnRMZ3chHn_9gkcrFuA',
    'https://www.youtube.com/feeds/videos.xml?channel_id=UC-QDfvrRIDB6F0bIO4I4HkQ',
    'https://www.youtube.com/feeds/videos.xml?channel_id=UCCezIgC97PvUuR4_gbFUs5g',
    'https://www.youtube.com/feeds/videos.xml?channel_id=UCA1piMIhFwAjIm-0Bofh9SA',
    'https://www.youtube.com/feeds/videos.xml?channel_id=UC4JX40jDee_tINbkjycV4Sg',
    'https://www.youtube.com/feeds/videos.xml?channel_id=UC_hPYclmFCIENpMUHpPY8FQ',
    'https://www.youtube.com/feeds/videos.xml?channel_id=UCWEHue8kksIaktO8KTTN_zg',
    'https://www.youtube.com/feeds/videos.xml?channel_id=UCRM1gWNTDx0SHIqUJygD-kQ'
]


def read_article_feed(feed):
    """Парсим и пробуем отправить ссылки в канал slack"""
    feeds = feedparser.parse(feed)
    for article in feeds['entries']:
        title, link = [article['title'], article['link']]
        if db.article_not_exist(article['title']):
            try:
                db.insert(title, link)
                bot.send_message(config.CHAT_ID, f"{title}\n{link}")
            except Exception as ex:
                print(ex)


def spin_feeds():
    """Перебираем все ссылки на фиды"""
    for x in myfeeds:
        read_article_feed(x)


schedule.every(60).minutes.do(spin_feeds)
while True:
    schedule.run_pending()
    time.sleep(1)
