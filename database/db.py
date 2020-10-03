import psycopg2
from psycopg2 import sql
import config


class Database():
    def __init__(self, database, user, password, host, port):
        self.conn = psycopg2.connect(
            database=database, user=user, password=password, host=host, port=port)
        self.cursor = self.conn.cursor()
        self.conn.autocommit = True
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS python_articles 
        (title VARCHAR(512) NOT NULL,
        article_link VARCHAR(512) NOT NULL);''')

    def insert(self, title, link):
        """Заносим данные по статье в базу данных"""
        insert = sql.SQL('INSERT INTO python_articles VALUES {}').format(
            sql.SQL(',').join(map(sql.Literal, [(title, link)]))
        )
        self.cursor.execute(insert)

    def article_not_exist(self, title):
        """Проверяем есть такая запись в базе данных"""
        self.cursor.execute(
            "SELECT NOT EXISTS(SELECT 1 FROM python_articles WHERE title=%s)", (title,))
        result = self.cursor.fetchone()[0]
        return result


db = Database(config.DATABASE, config.PGUSER,
              config.PGPASSWORD, config.HOST, config.PORT)
