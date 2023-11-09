from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import token 
from logging import basicConfig, INFO
import sqlite3, time

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
basicConfig(level=INFO)

connection = sqlite3.connect('users.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER,
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    created VARCHAR(255)
);
""")

start_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Курсы'),
    types.KeyboardButton('Контакты'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('Записаться'),
    types.KeyboardButton('Отправить номер', request_contact=True),
    types.KeyboardButton('Отправить локацию', request_location=True)
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

"Нужно реализовать функцию записи пользователя в нашу базу данных users при работе с коммандой /start. Если пользователь есть в базе, то его не записываете!"

@dp.message_handler(commands='start')
async def start(message:types.Message):
    cursor.execute(f"SELECT id FROM users WHERE id = {message.from_user.id};")
    result = cursor.fetchall()
    if result == []:
        cursor.execute(f"""INSERT INTO users VALUES(
            {message.from_user.id}, '{message.from_user.username}',
            '{message.from_user.first_name}', '{message.from_user.last_name}',
            '{time.ctime()}'                                        
        );""")
        cursor.connection.commit()
    await message.answer(f"Здравствуйте {message.from_user.full_name}, добро пожаловать в Geeks!", reply_markup=start_keyboard)
    print(message)

@dp.message_handler(text="О нас")
async def about_us(message:types.Message):
    await message.answer("Geeks Osh - это айти курсы в Оше, которая открылась в 2021 году")

@dp.message_handler(text="Контакты")
async def contacts(message:types.Message):
    await message.answer("Вот наши контакты:\n+996772343206 - Нурболот")

@dp.message_handler(text="Адрес")
async def address(message:types.Message):
    await message.reply("Наш адрес: Мырзалы Аматова 1Б (БЦ Томирис)")
    await message.answer_location(40.51930909205171, 72.80296442030333)
    with open('first_bot.py', 'rb') as python_file:
        await message.answer_document(python_file)

courses_buttons = [
    types.KeyboardButton('Backend'),
    types.KeyboardButton('Frontend'),
    types.KeyboardButton('Android'),
    types.KeyboardButton('iOS'),
    types.KeyboardButton('UX/UI'),
    types.KeyboardButton('Назад'),
]
courses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses_buttons)

@dp.message_handler(text="Курсы")
async def courses(message:types.Message):
    await message.reply("Вот наши курсы:", reply_markup=courses_keyboard)

@dp.message_handler(text="Backend")
async def backend(message:types.Message):
    await message.reply("Backend - это серверная сторона проекта")

@dp.message_handler(text="Frontend")
async def frontend(message:types.Message):
    await message.reply("Frontend - это лицевая сторона проекта")

@dp.message_handler(text="Android")
async def android(message:types.Message):
    await message.reply("Android - это операционная система")

@dp.message_handler(text="iOS")
async def ios(message:types.Message):
    await message.reply("iOS - это операционная система компании Apple")

@dp.message_handler(text="UX/UI")
async def uxui(message:types.Message):
    await message.reply("UX/UI - это дизайн сайта или проекта")

@dp.message_handler(text="Назад")
async def cancell(message:types.Message):
    await start(message)

class MailingState(StatesGroup):
    message = State()

@dp.message_handler(text="Рассылка")
async def mailing(message:types.Message):
    if message.from_user.id in [1324284905]:
        await message.reply("Введите свой текст для рассылки")
        await MailingState.message.set()
    else:
        await message.reply("У вас нету прав на рассылку")
@dp.message_handler(state=MailingState.message)
async def send_mailing(message:types.Message, state:FSMContext):
    await message.answer("Начинаю рассылку....")
    cursor.execute("SELECT id FROM users;")
    users_id = cursor.fetchall()
    print(users_id)
    for i in users_id:
        print(i[0])
        await bot.send_message(i[0], message.text)
        await message.answer("Рассылка окончена")
        await state.finish()

class SingUpState(StatesGroup):
    first_name = State()
    last_name = State()
    phone = State()
    direction = State()

@dp.message_handler(text="Записаться")
async def sign_courses(message:types.Message):
    await message.reply(f"{message.from_user.full_name}, для того чтобы записаться на курсы нужно заполнить следующие поля:\n(Имя,Фамилия,Номер,Направление)")
    await message.answer("Введите свое имя:")
    await SingUpState.first_name.set()

@dp.message_handler(state=SingUpState.first_name)
async def get_last_name(message:types.Message, state:FSMContext):
    await state.update_data(first_name=message.text)
    await message.answer("Введите фамилию:")
    await SingUpState.last_name.set()

@dp.message_handler(state=SingUpState.last_name)
async def get_phone_number(message:types.Message, state:FSMContext):
    await state.update_data(last_name=message.text)
    await message.answer("Введите свой номер телефона: ")
    await SingUpState.phone.set()

@dp.message_handler(state=SingUpState.phone)
async def get_direction(message:types.Message, state:FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Какое направлние вас интересует?")
    await SingUpState.direction.set()

@dp.message_handler(state=SingUpState.direction)
async def get_all_fields_send_signup(message:types.Message, state:FSMContext):
    await state.update_data(direction=message.text)
    result = await storage.get_data(user=message.from_user.id)
    print(result)
    await bot.send_message(-4091924505, f"Заявка на записьЖ\n{result['first_name']},\n{result['last_name']}\n{result['phone']},\n{result['direction']}")
    await message.answer("Ваши данные записаные ожидайте....")


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message:types.Message):
    await message.answer(f"{message.contact.phone_number}")

@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_location(message:types.Message):
    await message.answer(f"{message.location}")

@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply("Я вас не понял, введите /help")

executor.start_polling(dp)
