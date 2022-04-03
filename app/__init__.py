import logging

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from aiogram.dispatcher.webhook.aiohttp_server import (
    SimpleRequestHandler,
    setup_application,
)
from aiohttp import web

from .core import log
from .core.config import TelegramConfig
from .handlers import get_router

logger = logging.getLogger(__name__)
cfg = TelegramConfig()


def prepare_app() -> web.Application:
    """Prepare web application.

    Create Telegram instances and setup webapp handlers.
    """
    api_server = TelegramAPIServer.from_base(cfg.local_server_url, is_local=True)

    bot = Bot(
        token=cfg.token.get_secret_value(),
        parse_mode="HTML",
        session=AiohttpSession(api=api_server),
    )
    dp = Dispatcher()
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    router = get_router()
    dp.include_router(router)

    app = web.Application()
    handler = SimpleRequestHandler(dispatcher=dp, bot=bot)
    handler.register(app, path=cfg.webhook_path)
    setup_application(app, dp, bot=bot)

    return app


async def on_startup(bot: Bot):
    """Setup app on startup."""
    log.setup()
    logger.warning("Starting bot with %s", cfg)

    await bot.delete_webhook()
    await bot.set_webhook(f"{cfg.webhook_url}{cfg.webhook_path}")


async def on_shutdown(bot: Bot):
    """Tear down app on shutdown."""
    await bot.session.close()
    logger.warning("Bot stopped.")
