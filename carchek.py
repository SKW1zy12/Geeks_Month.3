import logging
from aiogram import Bot, Dispatcher, types, executor
import sqlite3
from config import token

Bot = Bot(token=token)
dp = Dispatcher(Bot)

connect = sqlite3.connect("cars.db")
cursor = connect.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS users (
               NUMBER TEXT,
               MARK TETX,
               MODEL TEXT,
               YEAR TEXT
);
""")


insert = [
    ("А123ВС", "Toyota", "Camry","2018"),
    ("К456МН","Ford","Focus","2020"),
    ("Е789ОР","Honda","Accord","2019"),
    ("У321ТХ","BMW","X5","2021"),
    ("М654УИ"," Mercedes-Benz","C-Class","2017"),
    ("Л987КП","Audi","A4","2016"),
    ("О432РС","Volkswagen","Golf","2022"),
    ("Т876АБ","Chevrolet","Malibu","2018"),
    ("Н543ЖУ","Kia","Optima","2020"),
    ("Р210ЮК","Nissan","Altima","2019"),
    ]
cursor.executemany("""INSERT INTO users ("NUMBER", "MARK", "MODEL", "YEAR") VALUES (?, ?, ?, ?)""", insert)

connect.commit()


