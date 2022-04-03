from aiogram import Router


def get_router() -> Router:
    from . import echo, start

    router = Router()

    router.include_router(start.router)
    router.include_router(echo.router)

    return router
