"""Write the press-ready image to the competition output directory."""

from pathlib import Path
from shutil import copyfile


def main() -> None:
    edition = Path(__file__).resolve().with_name("entry.png")
    destination = Path("/output/entry.png")
    destination.parent.mkdir(parents=True, exist_ok=True)
    copyfile(edition, destination)


if __name__ == "__main__":
    main()
