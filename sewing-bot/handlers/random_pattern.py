from aiogram import Router
from aiogram.types import Message
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram import F
import json
import random
from main import conn
from aiogram.fsm.context import FSMContext

router = Router()

def get_pattern():
    cur = conn.cursor()
    query = """
        SELECT title, source, price FROM pattern 
            ORDER BY RANDOM() LIMIT 1;
    """
    cur.execute(query)
    title, source, price = cur.fetchone()
    cur.close()

    hearts = '💚❤️🖤💜💙💖💛🧡🤍'
    heart = random.choice(hearts)
    message = f'Выкройка для вас{heart}\n\n<b>{title}</b>\nСтоимость: {price} руб\n\n<a href="{source}">Перейти на сайт</a>'
    return message

@router.message(F.text.lower() == "случайная выкройка", StateFilter(default_state))
async def send_random_pattern(message: Message, state: FSMContext):
    message_answer = get_pattern()
    await message.answer(message_answer)