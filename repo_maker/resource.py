import subprocess
from subprocess import CompletedProcess

import rich

from abc import ABC, abstractmethod


__all__ = ["GIT", "PIPENV"]


def run_command(command: str) -> CompletedProcess:
    return subprocess.run(command, shell=True, capture_output=True)
    print(response)
    return response.returncode == 0


class Resource(ABC):
    @property
    def base_command(self) -> str:
        raise NotImplementedError

    def installed(self) -> bool:
        return run_command(f"which {self.base_command}").returncode == 0

    @abstractmethod
    def init_if_exists(self) -> None:
        """Initialize the resource. Can have prompting."""


class GIT(Resource):
    base_command: str = "git"

    def init(self) -> bool:
        return run_command(f"{self.base_command} init").returncode == 0

    def init_if_exists(self) -> None:
        if not self.installed():
            return

        init_git = input("Do you want to init git? (y/n) ")
        if init_git == "y" and self.init():
            rich.print("Git initialized.")
        else:
            rich.print("No Git initialized.")


class PIPENV(Resource):
    base_command: str = "pipenv"

    def init(self, python_version: str = "3.9") -> bool:
        response = run_command(f"{self.base_command} --python {python_version}")
        if response.stderr:
            rich.print(response.stderr.decode("utf-8"))
            return True

        rich.print(f"Python {python_version} created.")
        return response.returncode == 0

    def init_if_exists(self) -> None:
        if not self.installed():
            return

        env = input("Do you want to create a pipenv environment? (y/n) ")
        if env == "y":
            python_version = input("Which python version? ")
            if self.init(python_version):
                return

        rich.print("No environment created.")
