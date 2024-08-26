import subprocess
import shlex
from typing import Callable, Optional


class CommandExecutor:
    def __init__(self, command: str, callback: Optional[Callable[[str], None]] = None):
        self.command = shlex.split(command)
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
                    self.callback(
                        f"Process exited with error code: {process.returncode}"
                    )
        except Exception as e:
            print(f"Error while processing: {e}")
