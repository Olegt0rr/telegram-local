from aiogram import Router
from aiogram.types import Message
from aiogram.utils.markdown import hbold

router = Router()


@router.message(commands=["start"])
async def command_start_handler(message: Message) -> None:
    """Handle /start command."""
    user = message.from_user
    text_lines = [
        f"Hi, {hbold(user.full_name)}!",
        "Try to send me something...",
    ]
    await message.answer("\n".join(text_lines))
