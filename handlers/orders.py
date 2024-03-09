from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext

from main import dp
from states.simple_order import SimpleOrder
from keyboards.order_keyboards import generate_yes_no_kb


@dp.message_handler(commands="start_order")
async def start_simple_order(message:Message):
    await message.reply("Хочешь бургер?",
                        reply_markup=generate_yes_no_kb("burger"))
    await SimpleOrder.first()

@dp.callback_query_handler(text="burger:yes",state=SimpleOrder.is_burger)
async def answer_burger_additive(callback:CallbackQuery,state:FSMContext):
    ...