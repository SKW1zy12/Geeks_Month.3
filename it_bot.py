from aiogram import Bot, Dispatcher,types,executor
from config import token
from logging import basicConfig, INFO



bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

start_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Курсы'),
    types.KeyboardButton('Контакты'),
    types.KeyboardButton('Адрес')
]
start_keyborad = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здраствуйте {message.from_user.full_name} добро пожаловать в Geeks!", reply_markup=start_keyborad)

@dp.message_handler(text="О нас")
async def about_us(message:types.Message):
    await message.answer("Geeks Osh - это айти курсы в оше, которая открылось в 2021 году")
@dp.message_handler(text="Контакты")
async def contacts(message:types.Message):
    await message.answer("Вот наши контакты:\n+996554616367 -Абдуллох")

@dp.message_handler(text="Адрес")
async def address(message:types.Message):
    await message.answer("Наш адресс: Мырзалы Аматова 16 (БЦ Томирис)")
    await message.answer_location(40.51930909205171, 72.80296442030333)
    with open('first_bot.py', 'rb') as python_file:
        await message.answer_document(python_file)

coureses_buttons = [
    types.KeyboardButton('Backend'),
    types.KeyboardButton('Frontend'),
    types.KeyboardButton('Android'),
    types.KeyboardButton('iOS'),
    types.KeyboardButton('UX/UI'),
    types.KeyboardButton('Назад')
]
coureses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*coureses_buttons)

@dp.message_handler(text="Курсы")
async def courses(message:types.Message):
    await message.reply("Вот ваши крусы", reply_markup=coureses_keyboard)

@dp.message_handler(text="Backend")
async def backend(message:types.Message):
    await message.reply("Backend - это серверная сторона проекта")

@dp.message_handler(text="Frontend")
async def frotend(message:types.Message):
    await message.reply("Frontend - это лицовая сторона проекта")

@dp.message_handler(text="Android")
async def andorid(message:types.Message):
    await message.reply("Андроид - это операционная система")

@dp.message_handler(text="iOS")
async def ios(message:types.Message):
    await message.reply("iOS - это операционная система компании Apple")

@dp.message_handler(text="UX/UI")
async def uxui(message:types.Message):
    await message.reply("UX/UI - это дизайн сайта или проекта")

@dp.message_handler(text="Назад")
async def cancell(message:types.Message):
    await start(message)


@dp.message_handler()
async def not_found(message:types.Message):
   await message.reply("Я вас не понял, введите /help")

executor.start_polling(dp)