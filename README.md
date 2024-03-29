# BardQuickLauncher
Python script that launches multiple XIVLauncher instances

I simply wanted to have a script to launch multiple accounts at the same time instead of manually doing it with XIVLauncher shortcuts. So in the end, I made this project to make my life more comfortable, with automatic OTP macro support included.

## Requirements
- Python 3.11 or above
- XIVLauncher (With "Auto Login" and "OTP macro support" enabled)
  - [BardToolBox](https://github.com/BardToolbox/BardToolbox-Release)

## Setup
1. Rename `config.json.example` to `config.json`
2. Fill in the values in `config.json`
3. Run the `index.py` script

## Support
Do you need help, you can always come and ask me in the `#support` channel.
<br>🔗 https://discord.gg/AlexFlipnote

## One Time Password support
> It's very limited at the moment, but I plan to add more.
- 1Password (Requires 1Password CLI installed)
  - Format: `1password:PROFILE_NAME`

## config.json values
> Anything marked with `*` is optional

| Key | Type | Description |
| --- | --- | --- |
| xivlauncher_path | str | Path to XIVLauncher |
| roaming_paths | dict[str, [str, null]] | Path to roamingPath (null = default settings and plugins) |
| sleep_time* | int | Time to wait before launching next account in seconds (defaults to 10 seconds) |
| profiles | list[] | List of profiles to launch |

### config:profiles

| Key | Type | Description |
| --- | --- | --- |
| account | str | Account name on XIVLauncher |
| roaming_path | str | Path name from the `roaming_paths` setting |
| main_account* | bool | If this is main and app should wait for you to press enter to continue with the rest. This is to make sure that XIVLauncher boots BardToolBox to allow multiboxing |
| display_name* | str | Display name for the profile in the terminal (affects nothing) |
| oauth* | str | Which oauth engine the account uses |
| steam* | bool | If the account is a steam account |
