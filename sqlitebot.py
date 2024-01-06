
from aiogram import Bot,Dispatcher,types,executor
from config import token
import sqlite3, time
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging

stroge = MemoryStorage()

bot = Bot(token=token)
dp = Dispatcher(bot, stroge=stroge)
logging.basicConfig(level=logging.INFO)

connect = sqlite3.connect('notes.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
               id PRIMARY KEY,
               chat_id TEXT,
               username TEXT,
               note_text TEXT,
               timestamp, TEXT 
);
""")

connect.commit()

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Привет {message.from_user.full_name} Введите команду /add_note ил же /get_notes")

class NotesState(StatesGroup):
    message = State()

@dp.message_handler(commands='add_note')
async def add_note(message:types.Message, ):
    await message.answer("Напишите что бы в хотели добавить в заметки")
    await NotesState.message.set()




executor.start_polling(dp)