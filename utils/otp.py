import subprocess

from typing import Optional
from urllib.request import urlopen, Request


class OTP:
    def __init__(self, *args: str):
        self._output = subprocess.run(
            [g for g in args],
            capture_output=True,
            text=True
        )

    @property
    def otp(self) -> Optional[str]:
        """ Returns the OTP code from the output. """
        if not self._output:
            return None
        if not self._output.stdout:
            return None
        return self._output.stdout.strip()

    def request(self) -> None:
        """ Sends a request to the FFXIV Launcher with the OTP code. """
        if not self.otp:
            raise ValueError("No OTP code or terminal output found.")
        if len(self.otp) != 6:
            raise ValueError(
                "Invalid OTP code, expected 6 digits, "
                f"got the following:\n{self.otp}"
            )

        try:
            urlopen(Request(
                f"http://127.0.0.1:4646/ffxivlauncher/{self.otp}",
            ))
        except Exception:
            print(
                "Failed to establish connection with the FFXIV Launcher.\n"
                "Make sure you have enabled OTP macro support in the settings."
            )


class OnePassword(OTP):
    def __init__(self, profile: str):
        super().__init__(
            "op", "item", "get", profile, "--otp"
        )
