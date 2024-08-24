import os
import sys
import pathlib
import zipfile
import subprocess
import shlex
import json
from datetime import datetime
from typing import Callable, Optional, Dict


class CommandExecutor:
    def __init__(
        self, command_str: str, callback: Optional[Callable[[str], None]] = None
    ):
        self.command = shlex.split(command_str)
        self.callback = callback if callback else self._default_cb

    def _default_cb(self, line: str) -> None:
        print(f"Output: {line}")

    def run(self) -> None:
        try:
            with subprocess.Popen(
                self.command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            ) as process:
                for line in process.stdout:
                    self.callback(line.strip())

                process.wait()

                if process.returncode != 0:
                    print(f"Process exited with error code: {process.returncode}")
        except Exception as e:
            print(f"Error while processing: {e}")


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
        config = {}
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


if __name__ == "__main__":
    openocd = OpenOcd()
    openocd.load_data("./test-data")
    source_dirs = openocd.source_dirs()
    if source_dirs:
        print(openocd.get_config(source_dirs[0]))
        openocd.flash(source_dirs[0])
