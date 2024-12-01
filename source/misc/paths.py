from typing import Final
from dataclasses import dataclass


@dataclass
class Paths:
    env: Final[str] = ".env"
    log_filename: Final[str] = "source/data/logs/bot_log.log"
