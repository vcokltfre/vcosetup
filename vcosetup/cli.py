from pathlib import Path
from sys import argv

from .components import gitignore, license, pyproject, docker


def run(args: list[str]) -> None:
    path = Path(".")

    pargs = []
    deps = []

    for arg in args:
        if arg.startswith(":"):
            print("Creating project: {}".format(arg[1:]))
            path = Path(arg[1:])
            path.mkdir()
        elif arg.startswith("-"):
            deps.append(arg[1:])
        else:
            pargs.append(arg)

    for arg in pargs:
        print(f"[{path}] Running step: {arg}")

        if arg == "license":
            license.run(path)
        elif arg == "gitignore":
            gitignore.run(path)
        elif arg == "py":
            print("  Creating python project")
            license.run(path)
            gitignore.run(path)
            pyproject.run(path, deps)
        elif arg == "bot":
            print("  Creating bot project")
            license.run(path)
            gitignore.run(path)
            pyproject.run(path, [*deps, "disnake", "loguru"])
        elif arg == "api":
            print("  Creating api project")
            license.run(path)
            gitignore.run(path)
            pyproject.run(path, [*deps, "fastapi", "uvicorn"])
        elif arg == "docker":
            docker.run(path, ("bot" if "bot" in args else "api"))

def main() -> None:
    run(argv[1:])
