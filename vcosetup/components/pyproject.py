from os import system
from pathlib import Path

def run(path: Path, deps: list[str]) -> None:
    system(f"cd {path} && git init -q && poetry init -n -q -l MIT " + " ".join([f"--dependency {dep}" for dep in set(deps + ["taskipy"])]))
