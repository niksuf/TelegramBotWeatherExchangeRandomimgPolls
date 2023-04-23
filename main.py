from aiogram import Bot, Dispatcher, executor
from config import telegram_token

# Создание объекта бота
bot = Bot(telegram_token)
dp = Dispatcher(bot)


# На старте в консоль писать сообщение
async def on_startup(_):
    print('Бот запущен!')


# Запуск бота
if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)
