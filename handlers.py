from aiogram import types
from aiogram.dispatcher.filters import Text
import requests
import random
import datetime
from main import bot, dp
from config import open_weather_token, exchange_rate_token
from keyboards import kb, kb_back
from contents import photos_arr, HELP_COMMANDS, polls_pool

weather_flag = False
exchange_flag = False


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="<b>Добро пожаловать</b> в мой телеграм бот!",
                         parse_mode='HTML',
                         reply_markup=kb)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP_COMMANDS)


@dp.message_handler(Text(equals='Помощь'))
async def send_help(message: types.Message):
    await message.answer(text=HELP_COMMANDS)


@dp.message_handler(Text(equals='Погода'))
async def send_weather(message: types.Message):
    global weather_flag
    weather_flag = True
    await message.answer(text='Напиши название города, и я пришлю прогноз погоды!',
                         reply_markup=kb_back)


@dp.message_handler(Text(equals='Курсы валют'))
async def send_exchange(message: types.Message):
    global exchange_flag
    exchange_flag = True
    await message.answer(text='Введите через пробел коды двух валют (например: "USD EUR" или "USD RUB")',
                         reply_markup=kb_back)


@dp.message_handler(Text(equals='Назад'))
async def main_menu(message: types.Message):
    await message.answer(text='Вы в главном меню!',
                         reply_markup=kb)


@dp.message_handler(Text(equals='Случайная картинка'))
async def random_img(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random.choice(photos_arr))


@dp.message_handler(commands=['poll'])
async def create_poll(message: types.Message):
    poll_question = random.choice(polls_pool)
    await bot.send_poll(chat_id=message.chat.id,
                        question=poll_question[0],
                        options=[poll_question[1],
                                 poll_question[2],
                                 poll_question[3],
                                 poll_question[4]],
                        is_anonymous=False,
                        allows_multiple_answers=True)


@dp.message_handler(Text)
async def weather_and_exchange(message: types.Message):
    global weather_flag
    if weather_flag is True:
        weather_flag = False
        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }
        try:
            r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={message.text}"
                             f"&appid={open_weather_token}&units=metric")
            data = r.json()
            city = data["name"]
            cur_weather = data["main"]["temp"]

            weather_description = data["weather"][0]["main"]
            if weather_description in code_to_smile:
                wd = code_to_smile[weather_description]
            else:
                wd = "Посмотри в окно, не пойму что там за погода!"

            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind = data["wind"]["speed"]
            sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
            sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
            length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - \
                                datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

            await message.reply(f"\U000023F1{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
                                f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
                                f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
                                f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\n"
                                f"Продолжительность дня: {length_of_the_day}\n",
                                reply_markup=kb)
        except:
            await message.reply("\U00002620 Проверьте название города \U00002620",
                                reply_markup=kb_back)
    global exchange_flag
    if exchange_flag is True:
        exchange_flag = False
        payload = {}
        headers = {"apikey": exchange_rate_token}
        coin1, coin2 = message.text.split()
        try:
            await message.reply("Получаю курсы валют...",
                                reply_markup=kb_back)
            r = requests.request("GET",
                                 f"https://api.apilayer.com/exchangerates_data/convert?to={coin2}&from={coin1}&amount=1",
                                 headers=headers,
                                 data=payload)
            # print(r.status_code)
            result = r.json()
            if result['success'] is True:
                await message.reply(f"Дата: {result['date']}\n"
                                    f"Из {result['query']['from']} в {result['query']['to']}\n"
                                    f"Текущий курс: {result['result']}",
                                    reply_markup=kb)
            else:
                await message.reply('Что-то пошло не так, попробуйте заново',
                                    reply_markup=kb)
        except:
            await message.reply("\U00002620 Проверьте название валют \U00002620",
                                reply_markup=kb_back)