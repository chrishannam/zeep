from configparser import ConfigParser
import typing as t
from pathlib import Path
import os

DEFAULT_HOME = str(Path.home())


def setup_config(ini_file: t.Union[str, None] = None) -> ConfigParser:
    if not ini_file:
        ini_file = os.path.join(DEFAULT_HOME, '.config', 'jocasta_config.ini')
    config = ConfigParser()
    config.read(ini_file)
    return config