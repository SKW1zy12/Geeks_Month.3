import logging
from aiogram import Bot, Dispatcher, types, executor
import sqlite3
from aiogram.types import ParseMode
from config import token

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(bot)
connect = sqlite3.connect("cars.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
               NUMBER TEXT,
               MARK TEXT,
               MODEL TEXT,
               YEAR TEXT
);
""")

insert = [
    ("А123ВС", "Toyota", "Camry", "2018"),
    ("К456МН", "Ford", "Focus", "2020"),
    ("Е789ОР", "Honda", "Accord", "2019"),
    ("У321ТХ", "BMW", "X5", "2021"),
    ("М654УИ", "Mercedes-Benz", "C-Class", "2017"),
    ("Л987КП", "Audi", "A4", "2016"),
    ("О432РС", "Volkswagen", "Golf", "2022"),
    ("Т876АБ", "Chevrolet", "Malibu", "2018"),
    ("Н543ЖУ", "Kia", "Optima", "2020"),
    ("Р210ЮК", "Nissan", "Altima", "2019"),
]
cursor.execute("""INSERT INTO users ("NUMBER", "MARK", "MODEL", "YEAR") VALUES (?, ?, ?, ?)""", insert)

connect.commit()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Введите номер машины:")

@dp.message_handler(lambda message: message.text.isalnum())
async def process_number(message: types.Message):
    user_input = message.text

    
    cursor.execute("SELECT * FROM users WHERE NUMBER=?", (user_input,))
    result = cursor.fetchone()

    if result:
        await message.answer(f"Информация о машине:{result}")
    else:
        await message.answer("Нет информации по указанному номеру.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)