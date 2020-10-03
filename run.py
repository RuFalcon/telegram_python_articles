from config import CHAT_ID
import feedparser
from database.db import db
from telegram_bot import bot
import schedule
import time
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)


myfeeds = [
    "https://realpython.com/atom.xml",
    'https://www.freecodecamp.org/news/tag/python/rss',
    'https://habr.com/ru/rss/hub/python/',
    'https://habr.com/ru/rss/hub/django/',
    'https://www.reddit.com/r/python/.rss',
    'https://dev.to/feed/tag/python',
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
                db.insert(article['title'], article['link'])
                bot.send_message(CHAT_ID, f"{title}\n {link}")
            except Exception as ex:
                print(ex)


def spin_feeds():
    """Перебираем все ссылки на фиды"""
    for x in myfeeds:
        read_article_feed(x)


schedule.every(30).minutes.do(spin_feeds)
while True:
    schedule.run_pending()
    time.sleep(1)
