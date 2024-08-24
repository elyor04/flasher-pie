import os
import sys
import pathlib
import zipfile

import subprocess
import shlex
import json

from datetime import datetime


class CommandExecutor:
    def __init__(self, command_str, callback=None):
        self.command = shlex.split(command_str)
        self.callback = callback if callback else self._default_cb

    def _default_cb(self, line):
        print(f"Output: {line}")

    def run(self):
        process = subprocess.Popen(
            self.command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
        )

        try:
            for line in process.stdout:
                self.callback(line.strip())
        except Exception as e:
            print(f"Error while processing output: {e}")
        finally:
            process.stdout.close()
            process.wait()

        # process = subprocess.Popen(
        #     self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        # )

        # for line in process.stdout:
        #     self.callback(line.strip())

        # process.stdout.close()
        # process.wait()

        # if process.returncode != 0:
        #     error = process.stderr.read()
        #     print(f"Error: {error.strip()}")
        # process.stderr.close()


class OpenOcd:
    @classmethod
    def load_data(cls, load_dir):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        data_dir = os.path.join(base_dir, "data")
        load_dir = os.path.abspath(load_dir)

        os.makedirs(data_dir, exist_ok=True)
        load_sources = [os.path.join(load_dir, src) for src in os.listdir(load_dir)]
        data_sources = os.listdir(data_dir)

        for source in map(pathlib.Path, load_sources):
            if (
                source.is_file()
                and (source.suffix == ".zip")
                and (source.stem not in data_sources)
            ):
                source_file = str(source.resolve())
                source_dir = os.path.join(data_dir, source.stem)

                with zipfile.ZipFile(source_file, "r") as _file:
                    _file.extractall(source_dir)

    @classmethod
    def source_dirs(cls):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        data_dir = os.path.join(base_dir, "data")
        os.makedirs(data_dir, exist_ok=True)

        _source_dirs = [os.path.join(data_dir, src) for src in os.listdir(data_dir)]
        return [src for src in _source_dirs if os.path.isdir(src)]

    @classmethod
    def get_config(cls, source_dir):
        config = dict()

        sources = [os.path.join(source_dir, src) for src in os.listdir(source_dir)]
        for source in map(pathlib.Path, sources):

            if source.is_file() and (source.suffix == ".hex"):
                config["data"] = str(source.resolve())

            elif source.is_file() and (source.suffix == ".json"):
                with open(str(source.resolve()), "r") as _file:
                    data = json.load(_file)

                    config["title"] = data.get("title")
                    config["flash"] = data.get("flash")
                    config["erase"] = data.get("erase")
                    config["version"] = data.get("version")
                    config["description"] = data.get("description")

                    date = datetime.fromtimestamp(data.get("date"))
                    config["date"] = date.strftime("%A, %B %d, %Y %I:%M %p")

        config["flash"] = config.get("flash").format(config.get("data"))
        return config

    @classmethod
    def flash(cls, source_dir, callback=None):
        config = cls.get_config(source_dir)
        executor = CommandExecutor(config.get("flash"), callback)
        executor.run()

    @classmethod
    def erase(cls, source_dir, callback=None):
        config = cls.get_config(source_dir)
        executor = CommandExecutor(config.get("erase"), callback)
        executor.run()


if __name__ == "__main__":
    OpenOcd.load_data("./test-data")
    source_dirs = OpenOcd.source_dirs()
    print(source_dirs)
