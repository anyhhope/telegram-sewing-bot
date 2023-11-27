from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram import Router
from aiogram.types import Message
from aiogram import F
from main import conn
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove
import re
import random

router = Router()

categories={
    'Платья': 'dresses',
    'Блузки': 'blouses',
    'Юбки': 'skirts'
}
difficulty={
    'Любая': '0',
    'Подходит для начинающих': '1',
    'Средняя сложность': '2',
    'Требуется опыт пошива': '3'
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
    'Любой': '0',
    'малый': '1',
    'средний/умеренный': '2',
    'оверсайз/свободный': '3'
}

def create_keyboard(categories):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for text, callback_data in categories.items():
        button = InlineKeyboardButton(text=str(text), callback_data=str(callback_data))
        keyboard.inline_keyboard.append([button])
    return keyboard

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
async def process_email_sent(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer(text='Email сохранен')
    await state.update_data(amount=1)
    await message.answer(text='Выберите <b>категорию выкройки</b> \n\n Чтобы отменить действие напишите Отмена', 
                         reply_markup = create_keyboard(categories))
    await state.set_state(FSMFillForm.fill_difficulty)

@router.message(StateFilter(FSMFillForm.fill_email))
async def warning_email(message: Message):
    await message.answer(text = 'Введите email в корректном формате \n\n Чтобы отменить действие напишите Отмена')

@router.callback_query(StateFilter(FSMFillForm.fill_difficulty), F.data.in_(list(categories.values())))
async def process_topic_sent(callback: CallbackQuery, state: FSMContext):
    await state.update_data(category=callback.data)
    await callback.message.answer(text='Категория выбрана')
    await state.update_data(amount=1)
    await callback.message.answer(text='Выберите <b>сложность пошива выкройки</b> \n\n Чтобы отменить действие напишите Отмена', 
                         reply_markup = create_keyboard(difficulty))
    await state.set_state(FSMFillForm.fill_season)

@router.callback_query(StateFilter(FSMFillForm.fill_season), F.data.in_(list(difficulty.values())))
async def process_topic_sent(callback: CallbackQuery, state: FSMContext):
    await state.update_data(difficulty=callback.data)
    await callback.message.answer(text='Сложность выбрана')
    await state.update_data(amount=1)
    await callback.message.answer(text='Выберите <b>сезон</b> \n\n Чтобы отменить действие напишите Отмена', 
                         reply_markup = create_keyboard(season))
    await state.set_state(FSMFillForm.fill_season)

@router.callback_query(StateFilter(FSMFillForm.fill_season), F.data.in_(list(season.values())))
async def process_topic_sent(callback: CallbackQuery, state: FSMContext):
    await state.update_data(season=callback.data)
    await callback.message.answer(text='Сезон выбран')
    await state.update_data(amount=1)
    await callback.message.answer(text='Выберите <b>стиль</b> \n\n Чтобы отменить действие напишите Отмена', 
                         reply_markup = create_keyboard(style))
    await state.set_state(FSMFillForm.fill_style)

@router.callback_query(StateFilter(FSMFillForm.fill_style), F.data.in_(list(style.values())))
async def process_topic_sent(callback: CallbackQuery, state: FSMContext):
    await state.update_data(style=callback.data)
    await callback.message.answer(text='Стиль выбран')
    await state.update_data(amount=1)
    await callback.message.answer(text='Выберите <b>объем изделия</b> \n\n Чтобы отменить действие напишите Отмена', 
                         reply_markup = create_keyboard(volume))
    await state.set_state(FSMFillForm.fill_volume)

@router.callback_query(StateFilter(FSMFillForm.fill_volume), F.data.in_(list(volume.values())))
async def process_topic_sent(callback: CallbackQuery, state: FSMContext):
    await state.update_data(volume=callback.data)
    await callback.message.answer(text='Объем выбран')
    await state.update_data(amount=1)
    await callback.message.answer(text='Введите <b>диапазон стоимости в рублях</b>\nВ формате "От 0 до 1000" \n\n Чтобы отменить действие напишите Отмена', 
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(FSMFillForm.fill_price)

def is_valid_price_format(s):
    pattern = r"^От \d+ до \d+$"
    return bool(re.match(pattern, s))

def get_key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key

@router.message(StateFilter(FSMFillForm.fill_price), 
               lambda message: is_valid_price_format(message.text))
async def process_email_sent(message: Message, state: FSMContext):
    await state.update_data(price = message.text)
    user_data = await state.get_data()
    text = f"Ваши данные\n\nФИО: <b>{user_data['fio']}</b>\nemail: <b>{user_data['email']}</b>\nКатегория: <b>{get_key(categories, user_data['category'])}</b>\nСложность: <b>{get_key(difficulty, user_data['difficulty'])}</b>\nСезон: <b>{get_key(season, user_data['season'])}</b>\nСтиль: <b>{get_key(style, user_data['style'])}</b>\nОбъем: <b>{get_key(volume, user_data['volume'])}</b>\nСтоимость: <b>{user_data['price']}</b>"
    await message.answer(text = text)

    cur = conn.cursor()
    query = """
        SELECT title, source, price FROM pattern 
        WHERE category = %s AND difficulty = %s AND season = %s AND
        style = %s AND volume = %s
        ORDER BY RANDOM() LIMIT 1;
    """

    params = (user_data['category'], user_data['difficulty'], user_data['season'], user_data['style'], user_data['volume'])
    cur.execute(query, params)
    row = cur.fetchone()
    if row is not None:
        title, source, price = row
    else:
        title, source, price = None, None, None
    cur.close()

    # query = "SELECT title, source, price FROM pattern WHERE "
    # params = []

    for key, field in user_data.items():
        print('key', key, 'field', field)

    hearts = '💚❤️🖤💜💙💖💛🧡🤍'
    heart = random.choice(hearts)
    text = f'Выкройка для вас{heart}\n\n<b>{title}</b>\nСтоимость: {price} руб\n\n<a href="{source}">Перейти на сайт</a>'
    await message.answer(text = text)

@router.message(StateFilter(FSMFillForm.fill_price))
async def warning_email(message: Message):
    await message.answer(text = 'Введите стоимоть в корректном формате \n\n Чтобы отменить действие напишите Отмена')
