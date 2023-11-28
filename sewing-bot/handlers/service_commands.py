from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram import F

router = Router()

start_keaboard = ReplyKeyboardBuilder()
start_keaboard.row(
    KeyboardButton(text="Случайная выкройка")
)
start_keaboard.row(KeyboardButton(
    text="Подобрать индивидуально",
))

@router.message(Command("start"))
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    answer_str = f"Привет, <b>{message.from_user.full_name}!</b>\nЯ помогу подобрать для тебя идеальную выкройку для пошива одежды! Начнем?\n"
    await message.answer(answer_str, reply_markup=start_keaboard.as_markup(resize_keyboard=True))

@router.message(F.text.lower()=='отмена', StateFilter(default_state))
async def process_cancel_command(message: Message, state: FSMContext):
    await message.answer(
        text="Уже уходите? До встречи)"
    )

@router.message(F.text.lower()=='отмена', ~StateFilter(default_state))
async def process_finish_command_any(message: Message, state: FSMContext):
    await message.answer(text = 'Отмена заполнения данных', reply_markup=start_keaboard.as_markup(resize_keyboard=True))
    await state.set_state(None)