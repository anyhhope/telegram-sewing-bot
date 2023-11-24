from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()


@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    answer_str = f"Привет, <b>{message.from_user.full_name}!</b>\nЯ помогу подобрать для тебя идеальную выкройку для пошива одежды! Начнем?"

    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text="Случайная выкройка")
    )
    builder.row(KeyboardButton(
        text="Подобрать индивидуально",
    ))
    await message.answer(answer_str, reply_markup=builder.as_markup(resize_keyboard=True))