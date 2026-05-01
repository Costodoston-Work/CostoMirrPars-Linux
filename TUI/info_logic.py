import os
from rich.console import Console

from TUI.all_panels import exit_panel, headline_panel, info_menu_panel
from TUI.exit_logic import exit_logic

console = Console()

def info_logic():
    os.system('clear')
    headline_panel()
    console.print("\nSelect the desired localization: ")
    info_menu_panel()

    selection_info_menu = input('\n(info menu) Choice: ')
    if selection_info_menu == '1':
        os.system('clear')
        os.system('python -m rich.markdown RU_INFO.md')
        console.print("")
        exit_panel()

        selection_info = input('\n(mirrors menu) Choiсe: ')

        if selection_info.casefold() == 'q':
            exit_logic()

        else:
            error()


    elif selection_info_menu == '2':
        os.system('clear')
        os.system('python -m rich.markdown EN_INFO.md')
        console.print("")
        exit_panel()

        selection_info = input('\n(mirrors menu) Choiсe: ')

        if selection_info.casefold() == 'q':
            exit_logic()

        else:
            error()

    else:
        error()

def error():
    os.system('clear')
    console.print('Wrong choice ❌\nTry again')
    console.print('\n\nPress "Enter" to continue ...')
    input()
    info_logic()