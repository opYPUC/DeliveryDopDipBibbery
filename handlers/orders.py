from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import FSMContext

from main import dp
from states.simple_order import SimpleOrder
from keyboards.order_keyboards import generate_yes_no_kb,what_burger_additive_kb,what_fries_additive_kb


@dp.message_handler(commands="start_order")
async def start_simple_order(message:Message):
    await message.reply("Хочешь бургер?",
                        reply_markup=generate_yes_no_kb("burger"))
    await SimpleOrder.first()

@dp.callback_query_handler(state=SimpleOrder.is_burger)
async def answer_burger_additive(callback:CallbackQuery,state:FSMContext):
    if callback.data == "burger:yes":
        await callback.message.edit_text(text="Выберите дополнение к бургеру",
                                         reply_markup=what_burger_additive_kb)
        await state.set_state(SimpleOrder.burger_additive.state)
        await state.update_data(burger=True)
    else:
        await callback.message.edit_text(text="Хочешь картошку?",
                                         reply_markup=generate_yes_no_kb("fries"))
        await state.set_state(SimpleOrder.is_french_fries.state)
        await state.update_data(burger=False)

@dp.callback_query_handler(state=SimpleOrder.burger_additive)
async def get_burger_additive(callback: CallbackQuery, state:FSMContext):
    if callback.data == "cheese":
        await callback.answer("Сыр успешно добавлен в заказ")
        await state.update_data(cheese=True)
    elif callback.data == "sauce":
        await callback.answer("Соус успешно добавлен в заказ")
        await state.update_data(sauce = True)
    elif callback.data == "end1":
        await callback.message.edit_text(text="Хочешь картошку?",
                                         reply_markup=generate_yes_no_kb("fries"))
        await state.set_state(SimpleOrder.is_french_fries.state)
        #TODO Сделать кол-во ингридеентов

@dp.callback_query_handler(state=SimpleOrder.is_french_fries)
async def answer_fries_additive(callback:CallbackQuery,state:FSMContext):
    if callback.data == "fries:yes":
        await callback.message.edit_text(text="Выберите дополнение к картошке",
                                         reply_markup=what_fries_additive_kb)
        await state.set_state(SimpleOrder.french_fries_additive.state)
        await state.update_data(fries=True)
    else:
        await state.update_data(fries=False)
        await pre_finish_order(callback,state)

@dp.callback_query_handler(state=SimpleOrder.french_fries_additive)
async def get_fries_additive(callback: CallbackQuery, state:FSMContext):
    if callback.data == "salt":
        await callback.answer("Соль успешно добавлена в заказ")
        await state.update_data(salt=True)
    elif callback.data == "sugar":
        await callback.answer("Сахар успешно добавлен в заказ")
        await state.update_data(sugar = True)
    elif callback.data == "end1":
        await pre_finish_order(callback,state)

async def pre_finish_order(callback:CallbackQuery,state:FSMContext):
    data = await state.get_data()
    print(data)
    text = ""
    if data["burger"]:
        text += "Бургер:"
        if data.get('cheese'):
            text += " сыр"
        if data.get('sauce'):
            text += " соус"
        text += "\n"
    if data["fries"]:
        text += "Картошка фри:"
        if data.get('salt'):
            text += " соль"
        if data.get('sugar'):
            text += " сахар"
        text += "\n"

    await callback.message.edit_text("Ваш заказ: \n" + text)
    await callback.message.delete_reply_markup()
    await state.finish()