# -*- coding: utf-8 -*-
import logging
import os


def setup_logging(subdir="logs"):
    """Creates a directory and logfile in it"""
    logdir_path = os.path.dirname(os.path.abspath(__file__))
    logfile_path = os.path.join(logdir_path, subdir, "bot.log")

    if not os.path.exists(os.path.join(logdir_path, subdir)):
        os.makedirs(os.path.join(logdir_path, subdir))

    logfile_handler = logging.handlers.WatchedFileHandler(logfile_path, 'a', 'utf-8')
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO,
                        handlers=[logfile_handler])
