import os
import sys
import pathlib
import zipfile

import json
from datetime import datetime
from typing import Callable, Optional, Dict

from .cmdExecutor import CommandExecutor


class OpenOcd:
    def __init__(self) -> None:
        self.base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.data_dir = os.path.join(self.base_dir, "data")
        os.makedirs(self.data_dir, exist_ok=True)

    def load_data(self, load_dir: str) -> None:
        load_dir = os.path.abspath(load_dir)
        load_sources = [
            pathlib.Path(os.path.join(load_dir, src)) for src in os.listdir(load_dir)
        ]
        data_sources = set(os.listdir(self.data_dir))

        for source in load_sources:
            if (
                source.is_file()
                and source.suffix == ".zip"
                and source.stem not in data_sources
            ):
                with zipfile.ZipFile(source, "r") as _file:
                    _file.extractall(os.path.join(self.data_dir, source.stem))

    def source_dirs(self) -> list[str]:
        return [
            os.path.join(self.data_dir, src)
            for src in os.listdir(self.data_dir)
            if os.path.isdir(os.path.join(self.data_dir, src))
        ]

    def get_config(self, source_dir: str) -> Dict[str, str]:
        config = dict()
        sources = [
            pathlib.Path(os.path.join(source_dir, src))
            for src in os.listdir(source_dir)
        ]

        for source in sources:
            if source.is_file():
                if source.suffix == ".hex":
                    config["data"] = str(source.resolve())
                elif source.suffix == ".json":
                    with open(source, "r") as _file:
                        data = json.load(_file)
                        config.update(
                            {
                                "title": data.get("title"),
                                "flash": data.get("flash"),
                                "erase": data.get("erase"),
                                "version": data.get("version"),
                                "description": data.get("description"),
                                "date": datetime.fromtimestamp(
                                    data.get("date")
                                ).strftime("%A, %B %d, %Y %I:%M %p"),
                            }
                        )

        if "flash" in config and "data" in config:
            config["flash"] = config["flash"].format(config["data"])

        return config

    def flash(
        self, source_dir: str, callback: Optional[Callable[[str], None]] = None
    ) -> None:
        config = self.get_config(source_dir)
        executor = CommandExecutor(config.get("flash", ""), callback)
        executor.run()

    def erase(
        self, source_dir: str, callback: Optional[Callable[[str], None]] = None
    ) -> None:
        config = self.get_config(source_dir)
        executor = CommandExecutor(config.get("erase", ""), callback)
        executor.run()
