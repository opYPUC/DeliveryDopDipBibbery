from aiogram import Dispatcher,Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.settings import BOT_TOKEN

memory = MemoryStorage()

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot,storage=memory)
