from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

def generate_yes_no_kb(type_q:str) -> InlineKeyboardMarkup:
    yes_no_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Да",callback_data=f"{type_q}:yes")
        ],
        [
            InlineKeyboardButton(text="Нет", callback_data=f"{type_q}:no")
        ]
    ])
    return yes_no_kb

what_burger_additive_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="сыр",callback_data="cheese")],
    [InlineKeyboardButton(text="соус",callback_data="sauce")]
])

what_fries_additive_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="соль",callback_data="salt")],
    [InlineKeyboardButton(text="сахар",callback_data="sugar")]
])