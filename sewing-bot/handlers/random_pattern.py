from aiogram import Router
from aiogram.types import Message
from aiogram import F
import json
import random
from main import conn

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

@router.message(F.text.lower() == "случайная выкройка")
async def send_travel_advice(message: Message):
    message_answer = get_pattern()
    await message.answer(message_answer)