import os
import sys

from rich.console import Console

from TUI.settings_logic import settings_logic

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from TUI.manual_menu.distribution_branch import distribution_branch
from TUI.info_logic import info_logic
from TUI.auto_logic import auto_logic
from TUI.exit_logic import exit_logic
from TUI.main_logic import main_logic

console = Console()

def run():
    os.system('clear')

    main_logic()

    selection_main_menu = input('\n(main menu) Choice: ')

    if selection_main_menu.casefold() == 'a':
        auto_logic()

    elif selection_main_menu.casefold() == 'm':
        distribution_branch()

    elif selection_main_menu.casefold() == 's':
        settings_logic()

    elif selection_main_menu.casefold() == 'i':
        info_logic()

    elif selection_main_menu.casefold() == 'q':
        exit_logic()

    else:
        os.system('clear')
        console.print('Wrong choice ❌\nTry again')
        console.print('\n\nPress "Enter" to continue ...')
        input()
        run()

if __name__ == "__main__":
    run()

