from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
weather_button = KeyboardButton('Погода')
exchange_button = KeyboardButton('Курсы валют')
random_img_button = KeyboardButton('Случайная картинка')
help_button = KeyboardButton('Помощь')
kb.add(weather_button).insert(exchange_button).insert(random_img_button).add(help_button)

kb_weather = ReplyKeyboardMarkup(resize_keyboard=True)
moscow_button = KeyboardButton('Москва')
spb_button = KeyboardButton('Санкт-Петербург')
izhevsk_button = KeyboardButton('Ижевск')
dmitrov_button = KeyboardButton('Дмитров')
weather_back_button = KeyboardButton('Назад')
kb_weather.add(moscow_button).insert(spb_button).insert(izhevsk_button).insert(dmitrov_button).\
    insert(weather_back_button)

kb_exchange = ReplyKeyboardMarkup(resize_keyboard=True)
usd_to_rub_button = KeyboardButton('USD RUB')
usd_to_eur_button = KeyboardButton('USD EUR')
exchange_back_button = KeyboardButton('Назад')
kb_exchange.add(usd_to_rub_button).insert(usd_to_eur_button).add(exchange_back_button)

kb_back = ReplyKeyboardMarkup(resize_keyboard=True)
back_button = KeyboardButton('Назад')
kb_back.add(back_button)
