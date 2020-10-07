Python article and video parser
=============================== 

Программа по сбору последних интересных новостей и видео, которые касаются языка программирования Python.

Работает следующим образом: 
- С помощью библиотеки feedparser каждый час обходит фиды и youtube-каналы посвящённые Python из заранее составленного списка.
- Проверяет есть ли новости в базе данных и если нет добавляет новость в базу и передаёт на отправку в telegram.
- Telegram бот присылвет новости в формате заголовок-ссылка в группу в telegram.

[Ссылка на рабочую группу](https://web.telegram.org/#/im?p=@python_articles_and_videos)

![Python: articles and videos](telegram.jpg "Python: articles and videos")


## Установка
Установка виртуального окружения
`python -m venv venv`

Установка зависимостей
`pip install -r requirements.txt`

## Создание переменных окружения
Перед запуском программы нужно создать файл .env и установить туда свои переменные окружения:
- TELEGRAM_API_TOKEN - Токен telegram бота
- CHAT_ID - чат id группы или бота в telegram
- DATABASE - название базы данных postgres
- PGUSER - имя пользователя postgres
- PGPASSWORD - пароль пользователя postgres
- HOST - ip-адрес
- PORT - порт

## Запуск программы
`python run.py`

## Запуск через Docker
`git clone https://github.com/RuFalcon/telegram_python_articles.git`

Создание .env файла и загрузка всех переменных окружения

`docker up --build`
