from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from handlers import add_habit, edit_habit, view_habits
import logging

API_TOKEN = 'YOUR_BOT_API_TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7678163374:AAHy-xfKIXgZYqzzydzkearFYbq5Xzi9kO4")
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

dp.register_message_handler(add_habit.start, commands="add_habit")
dp.register_message_handler(edit_habit.start, commands="edit_habit")
dp.register_message_handler(view_habits.show, commands="view_habits")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)