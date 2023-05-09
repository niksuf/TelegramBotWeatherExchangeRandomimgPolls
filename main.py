from aiogram import Bot, Dispatcher, executor
from config import telegram_token, proxy_url

bot = Bot(token=telegram_token, proxy=proxy_url)
# bot = Bot(token=telegram_token)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот запущен!')


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, on_startup=on_startup)
