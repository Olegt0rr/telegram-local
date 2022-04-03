import logging


def setup():
    from .config import LoggingConfig

    cfg = LoggingConfig()
    logging.basicConfig(**cfg.dict())
