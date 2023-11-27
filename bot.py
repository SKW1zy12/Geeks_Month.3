import logging
from config import token
from aiogram import Bot, Dispatcher, types , executor
import sqlite3



bot = Bot(token=token)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot)

connect = sqlite3.connect('practic.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
               ID PRIMARY KEY,
               NAME TEXT,
               LASTNAME TEXT,
               PHONE_NUMBER TEXT
);
""")

connect.commit()

insert = ("2007", "Abdulloh", "Tahirov", "0554616367")

cursor.execute("""INSERT INTO users("ID", "NAME", "LASTNAME", "PHONE_NUMBER") VALUES (?, ?, ?, ?)""", insert)

connect.commit()


@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Введите id пользавателя: ")


@dp.message_handler(lambda message: message.text.isalnum())
async def id(message:types.Message):
    user_input = message.text

    cursor.execute("SELECT * FROM users WHERE LASTNAME=?", (user_input),)
    result = cursor.fetchall()


    if result:
        await message.answer(f"информация о пользавателе: {result}")

    else :
        await  message.answer("Информация о пользавателе не найдена")
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)