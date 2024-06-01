"""
    Help command processor
"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from config import ADMIN_CHAT_ID, greet_kb

router = Router()


@router.message(Command("help", ignore_case=True))
async def cmd_help(message: Message):
    if message.from_user is not None:
        if str(message.chat.id) != ADMIN_CHAT_ID:
            await message.answer(
                "В данном боте, вы можете:\n"
                "1. Оставить отзыв о работе магазина! 🏪\n"
                "2. Есть возможность связаться с магазином. 🔗\n"
                "Для этого выберите соотвествующий пункт меню. 📋\n",
                reply_markup=greet_kb)
