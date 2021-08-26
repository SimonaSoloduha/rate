# rate

## Приложение для поиска курса валют

# Приложение может решить следующие задачи:
Получить актуальный курс украинской гривны 
Автоматически сохраняет полученный курс в базу данных  
Получить историю курсов из базы данных с возможностью отфильтровать по периоду и валюте

## Запуск проекта:

Откройте консоль

Перейдите в папку, в которой будет храниться проект

cd <путь до папки>

Склонируйте проект https://github.com/SimonaSoloduha/rate

перейдите в папку проекта cd rate

Создайте виртуальное окружение venv python3 -m venv venv

Активируйте виртуальное окружение venv source venv/bin/activate

Установите необходимые пакеты: pip3 install -r requirements.txt

(Все используемые библиотеки представлены в файле requirements.txt)

При необходимости обновите pip

(Если получите сообщение: WARNING: You are using pip version 20.2.3; however, version 21.2.1 is available. You should consider upgrading via the '..... flask/venv/bin/python3 -m pip install --upgrade pip' command.)

Создайте БД с помощью команд Python 

from app import db
db.create_all()

Запустите проект через консоль

flask run

Перейдете по ссыке http://127.0.0.1:5000/
