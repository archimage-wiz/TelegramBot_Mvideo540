"""
    Config global vars :)
    i know it's need class etc.
"""
import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

load_dotenv()

BOT_TOKEN: str = str(os.getenv("BOT_TOKEN"))
ADMIN_CHAT_ID: str = str(os.getenv("ADMIN_CHAT_ID"))
ADMIN_BUTTON_INFO_TEXT = "Информация для администратора"

FEEDBACK_TEXT = "Оставить отзыв\n⭐⭐⭐⭐⭐\n⭐⭐⭐⭐⭐"
CALLME_TEXT = "Связь с магазином 📞"
SCORES_VARIANTS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


bot = Bot(token=BOT_TOKEN)
router = Router()
dp = Dispatcher()
logging.basicConfig(level=logging.ERROR)

admin_button_info = KeyboardButton(text=ADMIN_BUTTON_INFO_TEXT)
admin_kb = ReplyKeyboardMarkup(keyboard=[[admin_button_info]],
                               resize_keyboard=True)

button_response = KeyboardButton(text=FEEDBACK_TEXT)
button_callme = KeyboardButton(text=CALLME_TEXT)
greet_kb = ReplyKeyboardMarkup(keyboard=[[button_response, button_callme]],
                               resize_keyboard=True)
