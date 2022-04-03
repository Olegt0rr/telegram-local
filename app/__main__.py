from aiohttp import web

from . import prepare_app
from .core.config import WebAppConfig

app = prepare_app()
web.run_app(app, **WebAppConfig().dict())
