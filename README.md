# BardQuickLauncher
Python script that launches multiple XIVLauncher instances

I simply wanted to have a script to launch multiple accounts at the same time instead of manually doing it with XIVLauncher shortcuts. So in the end, I made this project to make my life more comfortable, with automatic OTP macro support included.

## Requirements
- Python 3.11 or above
- [XIVLauncher](https://goatcorp.github.io/) (With "Auto Login" enabled)
  - [BardToolBox](https://github.com/BardToolbox/BardToolbox-Release)

## Setup
1. Rename `config.ini.example` to `config.ini`
2. Fill in the values in `config.ini`
3. Run the `index.py` script

## Support
Do you need help, you can always come and ask me in the `#support` channel.
<br>🔗 https://discord.gg/AlexFlipnote

## One Time Password support
> It's very limited at the moment, but I plan to add more.
- XIVLauncher "OTP macro support" enabled
- 1Password (Requires 1Password CLI installed)
  - Format: `1password:PROFILE_NAME`

## config.ini values
> Anything marked with `?` is optional

### [XIVLauncher]

| Key | Type | Description |
| --- | --- | --- |
| ?path | str | Path to XIVLauncher, defaults to %localappdata%\XIVLauncher\XIVLauncher.exe |
| ?sleep_time | int | Time to wait before launching next account in seconds (defaults to 10 seconds) |

### [roaming_paths]

| Key | Type | Description |
| --- | --- | --- |
| NAME | str | Path to roamingPath for custom plugin profiles. Name is used as the key in profiles for the `roaming_path` setting |

### [profiles.NAME]
> The account name is determined by the section name, so if your profile is called `profiles.awesome_account`, the account name will be `awesome_account`

| Key | Type | Description |
| --- | --- | --- |
| ?main | bool | If this is main and app should wait for you to press enter to continue with the rest. |
| ?roaming_path | str | Path name from the `roaming_paths` setting, if not present, uses default XIVLauncher settings |
| ?display_name | str | Display name for the profile in the terminal (affects nothing) |
| ?oauth | str | Which oauth engine the account uses |
| ?steam | bool | If the account is a steam account |
