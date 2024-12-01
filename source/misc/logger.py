import logging
import os, colorlog


async def logger_setup():
    log_filename = 'source/data/logs/bot_log.log'

    if os.path.exists(log_filename):
        os.remove(log_filename)

    log_formatter_file = logging.Formatter("%(levelname)s | %(asctime)s | %(filename)s:%(lineno)d | %(message)s")
    log_formatter_console = colorlog.ColoredFormatter(
        "%(log_color)s%(levelname)s%(reset)s \033[34m|\033[0m %(log_color)s%(asctime)s%(reset)s \033[34m|\033[0m %(log_color)s%(filename)s:%(lineno)d%(reset)s \033[34m|\033[0m %(log_color)s%(message)s%(reset)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        log_colors={
            'DEBUG': 'light_purple',
            'INFO': 'light_purple',
            'WARNING': 'light_yellow',
            'ERROR': 'red',
            'CRITICAL': 'light_red',
        }
    )

    file_log = logging.FileHandler(log_filename, "w", "utf-8")
    file_log.setFormatter(log_formatter_file)
    file_log.setLevel(logging.INFO)

    console_out = logging.StreamHandler()
    console_out.setFormatter(log_formatter_console)
    console_out.setLevel(logging.INFO)

    logging.basicConfig(handlers=(file_log, console_out),
                        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s | %(filename)s',
                        datefmt='%m.%d.%Y %H:%M:%S',
                        level=logging.INFO)
