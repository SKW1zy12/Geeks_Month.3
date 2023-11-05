from aiogram import Bot, Dispatcher, types,executor
from config import token

bot = Bot(token='6793875167:AAHpEes0i3NXpF8-hpgFigZ1JwfngG9CRzw')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет Гикс!! Python aiogram")

@dp.message_handler(commands='help')
async def help(message:types.Message):
    await message.answer("Чем я могу вам помочь?")

@dp.message_handler(text='Привет')
async def hello(message:types.Message):
    await message.answer("Привет как дела?")

@dp.message_handler(commands='test')
async def test(message:types.Message):
    await message.reply("Тест бота")
    await message.answer_location(10, 49)
    await message.answer_photo('https://i.ytimg.com/vi/0tlLsQkFL0Y/maxresdefault.jpg')
    await message.answer_dice()
    await message.answer_sticker('https://w7.pngwing.com/pngs/444/499/png-transparent-meme-illustration-face-rage-comic-internet-meme-me-gusta-meme-miscellaneous-comics-food.png')
    with open('test.jpg', 'rb') as test_jpg:
        await message.answer_photo(test_jpg)

executor.start_polling(dp)