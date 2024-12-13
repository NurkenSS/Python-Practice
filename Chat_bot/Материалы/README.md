Чат-бот для трекинга привычек

Проект разработан для синхронизации файлов между указанной локальной директорией и облачным хранилищем. Программа:
- Отслеживает изменения файлов на локальном компьютере.
- Загружает новые файлы в облачное хранилище.
- Обновляет изменённые файлы в облаке.
- Удаляет файлы из облачного хранилища при удалении их на компьютере.
- Логирует все действия в файл логов.


1. Установка и настройка окружения
1.1. Установка Python и PostgreSQL
Убедитесь, что на вашей машине установлены:
Python: версия 3.10 или выше.
PostgreSQL: Проверьте с помощью команд:

python3 --version
psql --version


1.2. Установка зависимостей

Создайте виртуальное окружение и установите все необходимые зависимости:

python3 -m venv venv
source venv/bin/activate  # Активировать виртуальное окружение

Установите зависимости проекта с помощью pip или Poetry.

Используя pip:
pip install -r requirements.txt

Используя Poetry:
poetry install


2. Настройка базы данных

2.1. Создание и настройка PostgreSQL базы данных

Убедитесь, что у вас установлен PostgreSQL и настроена база данных для проекта.

Пример конфигурации для базы данных в .env:
DATABASE_URL=postgresql://username:password@localhost/dbname

Замените username, password и dbname на ваши параметры.


2.2. Создание миграций базы данных

Для создания миграций базы данных используйте Alembic:

alembic init alembic  # если ещё не были созданы миграции
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head


3. Настройка Telegram бота

3.1. Получение токена для Telegram бота
	
1.	Откройте Telegram и найдите BotFather.
2.	Создайте нового бота и получите токен.

Добавьте токен в файл .env:

TELEGRAM_API_TOKEN=your_telegram_bot_token


4. Установка Webhook (если необходимо)

Для работы с Webhook настройте URL и сертификаты, следуя документации Telegram API.


5. Запуск проекта

5.1. Запуск приложения

Запустите сервер FastAPI для работы с API:
uvicorn app.main:app --reload


5.2. Запуск бота

Запустите бота с помощью кода, который будет подключаться к Telegram API:
habit_tracker_bot.py


6. Работа с ботом

6.1. Основные команды

•	/start — Запуск бота.
•	/trackhabit — Отслеживание привычки.
•	/setgoal — Установка цели.
•	/remind — Напоминания.
•	/status — Проверка статуса выполнения привычек.


6.2. Описание функционала

•	Бот позволяет отслеживать количество выполненных задач по каждой привычке.
•	Бот напомнит пользователю о привычке, если он не выполнил её в заданное время.
•	Бот генерирует отчеты по выполнению привычек.


7. Разработка

7.1. Добавление новой функциональности
1.	Добавьте новые команды в bot.py.
2.	Измените модели базы данных в models.py.
3.	Обновите логику работы с данными в services.py.


8. Контейнеризация с Docker

Если вы хотите запустить проект в контейнере Docker, выполните следующие шаги:
1.	Построите Docker-образ:
docker build -t chat-bot-for-habit-tracking .

2.	Запустите контейнер:
docker run -d -p 8000:8000 chat-bot-for-habit-tracking

Теперь сервер будет доступен на порту 8000.


9. Логирование
Проект использует стандартное логирование для отслеживания ошибок и событий. Логи можно будет найти в logs директории (если настроено).
