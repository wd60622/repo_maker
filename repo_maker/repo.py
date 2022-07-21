import os
from pathlib import Path

import typer

from repo_maker.resource import PIPENV, GIT
from repo_maker.utils import FILES_DIR


def create_module_name(repo_name: str):
    return repo_name.replace(" ", "_").replace("-", "_").lower()


class RepoAlreadyExistsError(Exception):
    pass


def create_repo(
    repo_name: str = typer.Argument(..., help="The name of the new repo"),
    in_root: bool = typer.Option(
        False, "--in-root", help="Whether you are currently in the root"
    ),
) -> None:
    """Create a new repo with boilerplate files."""
    cwd = Path.cwd()

    if in_root:
        repo_root = cwd
    else:
        repo_root = cwd / repo_name

        if repo_root.exists():
            raise RepoAlreadyExistsError("The repo already exists.")

        repo_root.mkdir()

        os.chdir(repo_root)

    PIPENV().init_if_exists()

    GIT().init_if_exists()

    # Create files in the root
    files = ["README.md", ".env.example", "Makefile"]
    for file in files:
        (repo_root / file).touch()

    sample_gitignore_lines = (FILES_DIR / "gitignore").read_text()
    (repo_root / ".gitignore").write_text(sample_gitignore_lines)

    module_name = create_module_name(repo_name)
    # Initialize all directories
    root_dirs = ["notebooks", module_name, "scripts", "tests", "data"]
    for root_dir in root_dirs:
        (repo_root / root_dir).mkdir()

    # Create files in the project directory
    files = ["__init__.py"]
    for file in files:
        (repo_root / module_name / file).touch()

    file_lines = (FILES_DIR / "utils.py").read_text()
    (repo_root / module_name / "utils.py").write_text(file_lines)
