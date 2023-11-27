from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram import Router
from aiogram.types import Message
from aiogram import F
from main import conn

router = Router()

categories={
    'Платья': 'dresses',
    'Блузки': 'blouses',
    'Юбки': 'skirts'
}
difficulty={
    'Любая': 0,
    'Подходит для начинающих': 1,
    'Средняя сложность': 2,
    'Требуется опыт пошива': 3
}
season={
    'Любой': 'none',
    'Весна-лето': 'summer',
    'Осень-зима': 'winter'
}
style={
    'Любой': 'none',
    'Повседневный': 'casual',
    'Вечерний': 'evening',
    'Официально-деловой': 'classic'
}
volume={
    'Любой': 0,
    'малый': 1,
    'средний/умеренный': 2,
    'оверсайз/свободный': 3
}
class FSMFillForm(StatesGroup):
    fill_fio = State()        # Состояние ожидания ввода фио
    fill_email = State()       # Состояние ожидания ввода почты
    fill_category = State()      # Состояние ожидания выбора категории   
    fill_difficulty = State()     # Состояние ожидания выбора сложности пошива
    fill_season = State()     # Состояние ожидания выбора сезона 
    fill_style = State() # Состояние ожидания выбора стиля
    fill_volume = State() # Состояние ожидания выбора объема одежды
    fill_price = State() # Состояние ожидания ввода цены на выкройку

# @router.message(F.text.lower() == "случайная выкройка", StateFilter(default_state))
# async def send_travel_advice(message: Message, state: FSMContext):
#     message_answer = get_pattern()
#     await message.answer(message_answer)