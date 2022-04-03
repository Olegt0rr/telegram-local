from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def echo_handler(message: Message) -> None:
    """Handle any message and send it back to user."""
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try, but I can't send it back to you! :)")
