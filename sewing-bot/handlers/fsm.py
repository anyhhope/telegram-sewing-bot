from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram import Router
from aiogram.types import Message
from aiogram import F
from main import conn
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove
import re

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
    choose_first = State()  # Состояние выбора первого действия
    fill_fio = State()        # Состояние ожидания ввода фио
    fill_email = State()       # Состояние ожидания ввода почты
    fill_category = State()      # Состояние ожидания выбора категории   
    fill_difficulty = State()     # Состояние ожидания выбора сложности пошива
    fill_season = State()     # Состояние ожидания выбора сезона 
    fill_style = State() # Состояние ожидания выбора стиля
    fill_volume = State() # Состояние ожидания выбора объема одежды
    fill_price = State() # Состояние ожидания ввода цены на выкройку

start_state_keaboard = ReplyKeyboardBuilder()
start_state_keaboard.row(
    KeyboardButton(text="Начать")
)
start_state_keaboard.row(
    KeyboardButton(text="Предыдущий результат")
)

@router.message(F.text.lower() == "подобрать индивидуально", StateFilter(default_state))
async def send_first_state_keyboard(message: Message, state: FSMContext):
    await message.answer('Выберите действие', reply_markup=start_state_keaboard.as_markup(resize_keyboard=True))
    await state.set_state(FSMFillForm.choose_first)

@router.message(F.text.lower() == "начать", StateFilter(FSMFillForm.choose_first))
async def send_first_state_keyboard(message: Message, state: FSMContext):
    await message.answer('Тогда начнем подбор)', reply_markup=ReplyKeyboardRemove())
    await message.answer(text='Пожалуйста, введите ваше <b>ФИО в три слова</b> \n\n Чтобы отменить действие напишите Отмена')
    await state.set_state(FSMFillForm.fill_fio)

@router.message(StateFilter(FSMFillForm.fill_fio), 
                lambda x: all(word.isalpha() for word in x.text.split()) and len(x.text.split()) == 3)
async def process_name_sent(message: Message, state: FSMContext):
    await state.update_data(fio=message.text)
    await message.answer(text='Имя сохранено')
    await state.update_data(amount=0)
    await message.answer(text='Введите ваш <b>email</b> \n\n Чтобы отменить действие напишите Отмена')
    await state.set_state(FSMFillForm.fill_email)

@router.message(StateFilter(FSMFillForm.fill_fio))
async def warning_name(message: Message):
    await message.answer(text = 'Введите ФИО в 3 слова \n\n Чтобы отменить действие напишите Отмена')

def is_valid_email(email: str) -> bool:
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.match(email_regex, email))

@router.message(StateFilter(FSMFillForm.fill_email), 
               lambda message: is_valid_email(message.text))
async def process_name_sent(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer(text='Email сохранен')
    await state.update_data(amount=1)
    await message.answer(text='Выберите <b>категорию выкройки</b> \n\n Чтобы отменить действие напишите Отмена')
    user_data = await state.get_data()
    await message.answer(text=f'{user_data["fio"]}')
    await state.set_state(FSMFillForm.fill_category)

@router.message(StateFilter(FSMFillForm.fill_email))
async def warning_name(message: Message):
    await message.answer(text = 'Введите email в корректном формате \n\n Чтобы отменить действие напишите Отмена')
    
