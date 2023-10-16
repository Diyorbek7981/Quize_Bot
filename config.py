from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

Token = '6312910209:AAFugcCgUqKPk3wfavJGx7vMxmT7U1FkvHQ'
bot = Bot(token=Token)
dp = Dispatcher(bot, storage=MemoryStorage())

CHANELS = ['@my_chanel_for_bot2', '@my_chanel_for_bot']
