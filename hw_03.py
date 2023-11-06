from aiogram import Bot, Dispatcher,types, executor
from config import token 
from logging import basicConfig, INFO

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)


start_buttons = [
    types.KeyboardButton("Меню"),
    types.KeyboardButton("О нас"),
    types.KeyboardButton("Адреcс"),
    types.KeyboardButton("Заказать еду")
]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Здарствуйте", reply_markup=start_keyboard)

@dp.message_handler(text="О нас")
async def abaut_us(message:types.Message):
    await message.answer("""Ocak Kebap
Кафе "Ожак Кебап" на протяжении 18 лет радует своих гостей с изысканными турецкими блюдами в особенности своим кебабом.

Наше кафе отличается от многих кафе своими доступными ценами и быстрым сервисом.

В 2016 году по голосованию на сайте "Horeca" были удостоены "Лучшее кафе на каждый день" и мы стараемся оправдать доверие наших гостей.

Мы не добавляем консерванты, усилители вкуса, красители, ароматизаторы, растительные и животные жиры, вредные добавки с маркировкой «Е». У нас строгий контроль качества: наши филиалы придерживаются норм Кырпотребнадзор и санэпидемстанции. Мы используем только сертифицированную мясную и рыбную продукцию от крупных поставщиков
""")

dp.message_handler(text="Адресc")
async def address(message:types.Message):
    await message.answer("Наш адресс")

executor.start_polling(dp)
