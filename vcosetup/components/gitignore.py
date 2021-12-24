from pathlib import Path

from requests import get


def run(path: Path) -> None:
    print("  Creating gitignore")
    content = get("https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore").text

    (path / ".gitignore").write_text(content)
