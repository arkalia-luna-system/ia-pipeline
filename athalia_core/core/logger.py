"""
Logger central pour athalia_core.
Réexporte une interface Logger compatible avec les scripts de maintenance/documentation.
"""

import logging


class Logger:
    """Wrapper autour du logger standard Python pour usage dans les scripts Athalia."""

    def __init__(self, name: str) -> None:
        self._logger = logging.getLogger(name)

    def info(self, msg: str, *args, **kwargs) -> None:
        self._logger.info(msg, *args, **kwargs)

    def warning(self, msg: str, *args, **kwargs) -> None:
        self._logger.warning(msg, *args, **kwargs)

    def error(self, msg: str, *args, **kwargs) -> None:
        self._logger.error(msg, *args, **kwargs)

    def debug(self, msg: str, *args, **kwargs) -> None:
        self._logger.debug(msg, *args, **kwargs)

    def exception(self, msg: str, *args, **kwargs) -> None:
        self._logger.exception(msg, *args, **kwargs)
