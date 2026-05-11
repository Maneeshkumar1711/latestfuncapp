import logging
from datetime import datetime, timezone

import azure.functions as func

from shared.config import AppConfig

logger = logging.getLogger(__name__)


def main(timer: func.TimerRequest) -> None:
    """
    Timer trigger entry point.

    Fires every 5 seconds
    Reads and logs configuration from environment variables.
    """
    utc_now = datetime.now(timezone.utc).isoformat()

    if timer.past_due:
        logger.warning("Timer is running past due.")

    config = AppConfig()

    logger.info(
        "Timer job running — app_name=%s, fired_at=%s",
        config.app_name,
        utc_now,
    )
