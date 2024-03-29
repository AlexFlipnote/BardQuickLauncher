import subprocess
import time

from typing import Optional, TYPE_CHECKING

from utils import otp, colours

if TYPE_CHECKING:
    from utils.config import Config


class FFXIV:
    def __init__(self, config: "Config", data: dict):
        self._config: "Config" = config

        self.account: str = data["account"]
        self.main_account: bool = bool(data.get("main_account", False))
        self.roaming_path: Optional[str] = data.get("roaming_path", None)
        self.steam: bool = bool(data.get("steam", False))
        self.oauth: Optional[str] = data.get("oauth", None)

        self.display_name: str = data.get("display_name", data["account"])

    def _otp_handler(self) -> Optional[otp.OTP]:
        """ Reads FFXIV.oauth value and returns the appropriate OTP handler. """
        if not self.oauth:
            return None

        option, value = (
            self.oauth.split(":")[0],
            "".join(self.oauth.split(":")[1:])
        )

        self.update_print(
            "Requesting OTP code...",
            colour="yellow"
        )

        match option.lower():
            case "1password":
                _output = otp.OnePassword(value)
            case _:
                _output = None

        return _output

    def update_print(
        self,
        text: str,
        colour: Optional[str] = None,
        end: Optional[str] = "\r"
    ) -> None:
        print(
            f"{self.display_name} | "
            f"{getattr(colours, colour or 'reset', colours.reset)}"
            f"{text}{colours.reset}",
            end=end
        )

    def launch(self) -> None:
        """ Launch the game with the specified profile. """
        _otp = self._otp_handler()

        output = [
            self._config.xivlauncher_path,
            f"--account={self.account}-{bool(self.oauth)}-{self.steam}"
        ]

        if self.roaming_path:
            _roaming_paths = self._config.roaming_paths.get(
                self.roaming_path
            )

            if _roaming_paths:
                output.append(f"--roamingPath={_roaming_paths}")

        subprocess.Popen(output)

        if _otp:
            self.update_print("Applying OTP code...", colour="yellow")
            time.sleep(3)
            _otp.request()

        self.update_print(
            f"Done!{' ' * 20}",
            colour="green",
            end=None
        )
