import os

from typing import Optional, Any


def print_stop(
    text: str,
    status: int = 0
) -> None:
    """
    Uses input() to print a message and then exit the program
    """
    input(text)
    exit(status)


def clear_terminal(
    text: Optional[str] = None
) -> None:
    """
    Clears the terminal screen
    """
    os.system("cls" if os.name == "nt" else "clear")
    if text:
        print(text)


def get_int(data: dict, key: str, default: Any = 0) -> int:
    """
    Gets an integer from a dictionary, or returns a default value
    """
    try:
        return int(data.get(key, default))
    except ValueError:
        return -1
