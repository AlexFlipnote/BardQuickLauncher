import os

from typing import Optional

from . import misc, colours
from .ffxiv import FFXIV


class RoamingPaths:
    def __init__(self, data: dict):
        self._paths: dict[str, Optional[str]] = data

    def get(self, key: str) -> Optional[str]:
        return self._paths.get(key, None)


class Config:
    def __init__(self, data: dict):
        self.xivlauncher_path: str = data["xivlauncher_path"]
        self.sleep_time: int = data.get("sleep_time", 10)
        self.roaming_paths: RoamingPaths = RoamingPaths(data.get("roaming_paths", {}))

        self.profiles: list[FFXIV] = sorted(
            [FFXIV(config=self, data=p) for p in data["profiles"]],
            key=lambda x: x.main_account, reverse=True
        )

    @property
    def pretty_profiles(self):
        return "\n".join([
            f"{str(i).rjust(2)} | {p.display_name}"
            for i, p in enumerate(self.profiles, start=1)
        ])

    def validate_path(self) -> None:
        if os.path.exists(self.xivlauncher_path):
            return None

        misc.print_stop(
            f"{colours.red}Error:{colours.reset} XIVLauncher path not found, please check your config.json file\n"
            f"Path: {self.xivlauncher_path}",
            status=1
        )
