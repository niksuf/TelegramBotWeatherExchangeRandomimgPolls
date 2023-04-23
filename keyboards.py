# Файл с клавиатурами
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Основная клавиатура
kb = ReplyKeyboardMarkup(resize_keyboard=True)
weather_button = KeyboardButton('Погода')
exchange_button = KeyboardButton('Курсы валют')
random_img_button = KeyboardButton('Случайная картинка')
help_button = KeyboardButton('Помощь')
kb.add(weather_button).insert(exchange_button).insert(random_img_button).add(help_button)

# Клавиатура для возвращения в основное меню
kb_back = ReplyKeyboardMarkup(resize_keyboard=True)
back_button = KeyboardButton('Назад')
kb_back.add(back_button)
