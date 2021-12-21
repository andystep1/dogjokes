from typing import AnyStr, Text
import aiogram

from time import time
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from emoji import demojize

from config import TOKEN
from functions import get_keyboard
from functions import get_anek
from functions import get_dog

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    await message.reply(f'Привет! {user_name}! Нажми на кнопку', reply_markup=get_keyboard())


@dp.message_handler(lambda message: demojize(message.text) == ':dog:')
async def start(message: types.Message):
    await message.answer_photo(get_dog())

@dp.message_handler(lambda message: demojize(message.text) == ':rolling_on_the_floor_laughing:') 
async def start(message: types.Message):
    await message.reply(get_anek())

@dp.message_handler(lambda message: demojize(message.text) == ':dog: :rolling_on_the_floor_laughing:') 
async def start(message: types.Message):
    await message.answer_photo(get_dog())
    await message.reply(get_anek())

if __name__ == '__main__': #всегда тру
    executor.start_polling(dp)