import os
import re
import configparser

from typing import Optional

from . import misc, colours
from .ffxiv import FFXIV

re_profiles = re.compile(r"profiles\.([a-zA-Z0-9]{1,})")


class RoamingPaths:
    def __init__(self, data: dict):
        self._paths: dict[str, Optional[str]] = data

    def get(self, key: str) -> Optional[str]:
        return self._paths.get(key, None)


class Config:
    def __init__(self):
        data = configparser.ConfigParser()
        try:
            data.read("./config.ini")
        except FileNotFoundError:
            misc.print_stop("'config.ini' file not found, please create one.")

        _xivlauncher = dict(data).get("XIVLauncher", {})
        self.xivlauncher_path: str = _xivlauncher.get(
            "path", f"{os.getenv('LOCALAPPDATA')}\\XIVLauncher\\XIVLauncher.exe"
        )

        self.sleep_time: int = misc.get_int(_xivlauncher, "sleep_time", 10)

        self.roaming_paths: RoamingPaths = RoamingPaths(
            dict(data).get("roaming_paths", {})
        )

        _find_profiles: list[re.Match] = []
        for g in data.sections():
            if not re_profiles.match(g):
                continue
            _find_profiles.append(re_profiles.match(g))

        self.profiles: list[FFXIV] = sorted(
            [
                FFXIV(config=self, data=data[p[0]], account=p.group(1))
                for p in _find_profiles
            ],
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
            f"{colours.red}Error:{colours.reset} XIVLauncher path not found, "
            "please check your config.json file\n"
            f"Path: {self.xivlauncher_path}",
            status=1
        )
