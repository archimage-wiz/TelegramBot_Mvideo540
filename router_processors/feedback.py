"""
    Feedback processing routers
"""
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, or_f
from config import bot, FEEDBACK_TEXT, SCORES_VARIANTS
from common import MakeFeedback, send_admin_message

router = Router()


# alternative way for combinig "OR"
# @router.message(Command(commands=["feedback"]))
# @router.message(F.text == FEEDBACK_TEXT)
@router.message(
    or_f(Command(commands=["feedback"], ignore_case=True),
         F.text == FEEDBACK_TEXT))
async def cmd_feedback(message: Message, state: FSMContext):
    """
    Handles the "feedback" command message.

    Args:
        message (types.Message): The message object representing the command.

    Returns:
        None
    """
    await state.set_state(MakeFeedback.writing_feedback)
    await message.answer(
        "Напишите Ваш отзыв о магазине и впечатлениях полученных во время "
        "консультации нашими специалистами.")


@router.message(MakeFeedback.writing_feedback)
async def get_feedback(message: Message, state: FSMContext):
    """
    Asynchronously handles the "get_feedback" message event.

    Args:
        message (aiogram.types.Message):
            The message object representing the user's feedback.
        state (aiogram.dispatcher.FSMContext): The FSM context object.

    Description:
        This function is an event handler for the "get_feedback" message event.
        It updates the FSM context with the user's feedback,
        sends a confirmation message to the user, and
        sets the state to "MakeFeedback.setting_score".

        Parameters:
            - message (aiogram.types.Message):
                The message object representing the user's feedback.
            - state (aiogram.dispatcher.FSMContext): The FSM context object.
    """
    if message.text is not None:
        await state.update_data(feedback=message.text)
        await message.answer(
            text="Спасибо, Теперь пожалуйста поставьте оценку от 1 до 10.\n"
            "Где 10 - это Отлично, 1 - очень плохо.")
        await state.set_state(MakeFeedback.setting_score)


@router.message(MakeFeedback.setting_score, F.text.in_(SCORES_VARIANTS))
async def get_score(message: Message, state: FSMContext):
    """
    Asynchronously handles the "get_score" message event.

    Parameters:
        - message (aiogram.types.Message):
            The message object representing the user's feedback.
        - state (aiogram.dispatcher.FSMContext): The FSM context object.

    Returns:
        None
    """
    if message.text is not None:
        await state.update_data(score=int(message.text))
        await message.answer("Спасибо за отзыв!")
        feedback_data = await state.get_data()
        if message.from_user is not None:
            await send_admin_message(
                bot, "Пользователь:\n"
                F"UserID: {message.from_user.id}\n"
                F"Username: {message.from_user.username}\n"
                F"Name: {message.from_user.first_name} {message.from_user.last_name}\n"
                "оставил отзыв с оценкой.")
            await send_admin_message(
                bot, F"Оценка: {feedback_data['score']}\n"
                F"Отзыв: {feedback_data['feedback']}\n")
    await state.clear()
