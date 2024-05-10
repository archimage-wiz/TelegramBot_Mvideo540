"""
    CallBack processor routers
"""
from aiogram import Router, F
from aiogram.types import Message
from config import bot, CALLME_TEXT
from common import send_admin_message

router = Router()


@router.message(F.text == CALLME_TEXT)
async def cmd_callme(message: Message):
    """
    Handles the "callme" command message.

    Args:
        message (types.Message): The message object representing the command.

    Returns:
        None
    """
    if message.from_user is not None:
        await send_admin_message(
            bot,
            F"Пользователь:\n"
            F"ID: {message.from_user.id}\n"
            F"Username: {message.from_user.username}\n"
            F"Name: {message.from_user.first_name} {message.from_user.last_name}\n"
            F"Хочет чтобы с ним связались!"
        )
    await message.answer("Спасибо, мы c вами свяжемся через телеграм!")
