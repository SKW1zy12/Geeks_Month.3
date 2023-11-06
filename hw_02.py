from aiogram import Bot, Dispatcher,types,executor
from config import token
from logging import basicConfig, INFO



bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

start_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Обьекты'),
    types.KeyboardButton('Контакты')
]
start_keyborad = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Здраствуйте")

@dp.message_handler(text="О нас")
async def about_company(message:types.Message):
    await message.answer("Stroy.kg – это нишевое информационное агентство, которое публикует новости о строительстве и недвижимости в Кыргызстане")
@dp.message_handler(text="Обьекты")
async def object(message:types.Message):
    await message.answer("""Строительство ЖД «Курчатова» вышло на 12 этаж
В строящемся жилом доме «Курчатова» готова плита перекрытия 11 этажа. Об этом говорится в сообщении компании-застройщика «Action». Также готова опалубка колонн для плиты перекрытия 12 этажа, производятся фахверки 8 этажа. На 7 этаже фахверки уже установили, на 6 этаже – подали бетон и укладывают кирпич, а на 5 этаже кладка кирпича завершена. Жилой дом «Курчатова» имеет 14 этажей и находится в Нижнем Джала. Сдача ПСО ожидается в 2024 году.""")
    await message.answer_photo('https://stroy.kg/content/images/2023/11/-3-7.jpeg')
    await message.answer_photo('https://stroy.kg/content/images/2023/11/-4-7.jpeg')
    await message.answer_photo('https://stroy.kg/content/images/2023/11/-5-7.jpeg')
@dp.message_handler(text="Контакты")
async def conntact(message:types.Message):
    await message.answer("Наши контакты:+996(990)910110")

executor.start_polling(dp)