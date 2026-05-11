import os
import logging

logger = logging.getLogger(__name__)


class AppConfig:
    """
    Reads application configuration from environment variables.
    """

    def __init__(self) -> None:
        self.app_name: str = self._require("APP_NAME")

    @staticmethod
    def _require(key: str) -> str:
        value = os.getenv(key, "").strip()
        if not value:
            raise RuntimeError(
                f"Required environment variable '{key}' is not set or empty."
            )
        return value
