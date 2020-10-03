from database.db import db
import feedparser
import psycopg2
import config


def test_create_table():
    conn = psycopg2.connect(database=config.DATABASE, user=config.PGUSER,
                            password=config.PGPASSWORD, host=config.HOST, port=config.PORT)
    cursor = conn.cursor()
    cursor.execute('select * from python_articles')
    assert True == bool(cursor.rowcount)


def test_insert_feeds_data():
    db.insert('Яндекс', "http://yandex.ru/")
    assert False == db.article_not_exist('Яндекс')
