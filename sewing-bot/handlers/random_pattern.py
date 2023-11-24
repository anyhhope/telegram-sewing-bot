from aiogram import Router
from aiogram.types import Message
from aiogram import F
import json
import random

router = Router()

def get_pattern():
    return ''

@router.message(F.text.lower() == "случайная выкройка")
async def send_travel_advice(message: Message):
    message_answer = get_pattern()
    await message.answer(message_answer)