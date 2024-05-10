"""
    Common functions
"""
from aiogram import Bot
from aiogram.fsm.state import StatesGroup, State
from config import ADMIN_CHAT_ID


class MakeFeedback(StatesGroup):
    """
        Doc: State Class
    """
    writing_feedback = State()
    setting_score = State()


async def send_admin_message(bot: Bot, text: str):
    """
    Asynchronously sends an admin message
    with the provided text to the specified chat ID.

    Args:
        text (str): The text of the message to be sent.

    Returns:
        None
    """
    if ADMIN_CHAT_ID is not None:
        if text is not None:
            await bot.send_message(ADMIN_CHAT_ID, text)
