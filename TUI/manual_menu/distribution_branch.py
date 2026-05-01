import sys
import os
from rich.console import Console

from TUI.manual_menu.selection_distribution import selection_distribution

console = Console()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from TUI.all_panels import manual_menu_distribution_branch_panel
from TUI.all_panels import headline_panel

def distribution_branch():
    os.system('clear')
    headline_panel()
    console.print("\nSelect the based distribution branch:")
    manual_menu_distribution_branch_panel()  # Список веток (пока только Arch)
    selection_branch = input('\n(distribution branch menu) Выбор: ')

    if selection_branch == '1':
        selection_distribution()

    elif selection_branch.casefold() == 'q':
        os.system('clear')
        exit()


    else:
        os.system('clear')
        console.print('Wrong choice ❌\nTry again')
        console.print('\n\nPress "Enter" to continue ...')
        input()
        distribution_branch()