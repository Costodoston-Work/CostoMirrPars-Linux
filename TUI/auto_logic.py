import sys
import os

from mirrorlist.paste_mirrors_in_config.logic_for_copy_all_mirrors_in_configs import \
    logic_for_copy_all_mirrors_in_configs

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from TUI.all_panels import headline_panel, copy_exit_panel
from auto_detection_mirrors import system_verification
from TUI.exit_logic import exit_logic
from TUI.all_panels import exit_panel

from rich.console import Console

console = Console()

def auto_logic():
    os.system('clear')
    headline_panel()
    console.print("\n # Check result:", style = 'bold #FFA500')
    system_verification()
    console.print("")
    copy_exit_panel()

    selection_after_parsing = input('\n(mirrors menu) Choiсe: ')

    if selection_after_parsing.casefold() == 'c':
        logic_for_copy_all_mirrors_in_configs()
        print("")
        exit_panel()
        print("")
        selection_after_copy_mirrors = input('(after copy menu) Choiсe: ')

        if selection_after_copy_mirrors.casefold() == 'q':
            exit_logic()

        else:
            error()

    elif selection_after_parsing.casefold() == 'q':
        exit_logic()

    else:
        error()

def error():
    os.system('clear')
    console.print('Wrong choice ❌\nTry again')
    console.print('\n\nPress "Enter" to continue ...')
    input()
    auto_logic()
