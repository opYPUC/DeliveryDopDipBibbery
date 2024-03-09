from aiogram.dispatcher.filters.state import StatesGroup,State

class SimpleOrder(StatesGroup):
    is_burger = State()
    burger_additive = State()
    is_french_fries = State()
    french_fries_additive = State()
