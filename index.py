import json
import time

from utils import colours, misc
from utils.config import Config

with open("./config.json", "r", encoding="utf-8") as f:
    config = Config(json.load(f))

config.validate_path()

_credits = (
    f"{colours.blue}[ {colours.reset}BardQuickLauncher (BQL) v1.0.0 {colours.blue}]{colours.reset}\n"
    f"  - Created by AlexFlipnote{colours.reset}\n\n"
)

print(
    f"{_credits}Which profile do you want to launch?\n"
    f"{colours.yellow}Hint:{colours.reset} Type the number or 'exit', and press enter\n\n"
    " 0 | Launch all profiles\n"
    f"{'-' * 30}\n"
    f"{config.pretty_profiles}\n"
)


def main() -> None:
    should_exit_loop: bool = False

    while not should_exit_loop:
        match input("> ").strip().lower():
            case "exit":
                exit()

            case "0":
                should_exit_loop = True
                misc.clear_terminal(_credits)
                for i, p in enumerate(config.profiles):
                    if i != 0:
                        p.update_print("Waiting...", colour="yellow")
                        time.sleep(config.sleep_time)

                    p.update_print("Launching...", colour="yellow")
                    p.launch()

                    if p.main_account:
                        input(
                            f"\nMain account detected, press {colours.blue}enter{colours.reset} when you're in the main menu\n"
                            "(This is to prevent XIVLauncher refusing more than 2 instances of the game)\n"
                        )

            case x if x.isdigit():
                try:
                    p = config.profiles[int(x) - 1]
                    should_exit_loop = True
                    misc.clear_terminal(_credits)
                except IndexError:
                    print("Invalid choice, please try again.")
                    continue

                p.update_print("Launching...", colour="yellow")
                p.launch()

            case _:
                pass


try:
    main()
    input("\nEverything has been launched, press enter to exit.")
except KeyboardInterrupt:
    pass
