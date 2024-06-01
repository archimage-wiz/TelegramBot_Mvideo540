"""
    Welcome processor
"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from config import ADMIN_CHAT_ID, greet_kb, admin_kb

router = Router()


@router.message(Command("start", ignore_case=True, ignore_mention=True))
async def cmd_start(message: Message):
    """
    Handles the "start" command message.

    Args:
        message (types.Message): The message object representing the command.

    Returns:
        None
    """
    if message.from_user is not None:
        if str(message.chat.id) != ADMIN_CHAT_ID:
            await message.answer(
                F"Добрый день, {message.from_user.full_name}.\n"
                "Вас приветствует Магазин Мвидео, Лотос Плаза.😊!\n"
                "Вы можете оставить отзыв, о работе магазина 🏪.\n"
                "Связаться с нами можно нажав соответствующую кнопку в меню.\n",
                reply_markup=greet_kb)
        else:
            await message.answer("Привет, возможно сделать админку :)",
                                 reply_markup=admin_kb)
