import os


__all__ = ["GIT", "PYENV"]


class Resource:
    @property
    def base_command(self) -> str:
        raise NotImplementedError

    def installed(self) -> bool:
        return os.system(f"which {self.base_command}") == 0


class GIT(Resource):
    base_command: str = "git"

    def init(self) -> bool:
        return os.system(f"{self.base_command} init") == 0

    def init_if_exists(self) -> None:
        if not self.installed():
            return

        init_git = input("Do you want to init git? (y/n) ")
        if init_git == "y" and self.init():
            print("Git initialized.")
        else:
            print("No Git initialized.")


class PYENV(Resource):
    base_command: str = "pipenv"

    def init(self, python_version: str = "3.9") -> bool:
        return os.system(f"{self.base_command} --python {python_version}") == 0

    def init_if_exists(self) -> None:
        if not self.installed():
            return

        env = input("Do you want to create a pipenv environment? (y/n) ")
        if env == "y":
            python_version = input("Which python version? ")
            # TODO: get this check to work
            if self.init(python_version):
                print(f"Python {python_version} created.")
                return

        print("No environment created.")
