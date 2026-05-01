import sys
import os

from rich.console import Console

from TUI.manual_menu.selection_location import select_arch_locale_mirrors, select_artix_locale_mirrors, \
    select_cachyos_locale_mirrors

console = Console()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from TUI.all_panels import manual_menu_arch_distribution_panel
from TUI.all_panels import headline_panel
from TUI.exit_logic import exit_logic

def selection_distribution():

    os.system('clear')
    headline_panel()
    console.print("\nSelect a distribution:")
    manual_menu_arch_distribution_panel()
    # Список дистрибутивов на основе Arch

    selection_distribution_menu = input('\n(distribution menu) Choice: ')

    # ARCH
    if selection_distribution_menu == '1': # Если Arch дистрибутив, то
        select_arch_locale_mirrors()

    #ARTIX
    elif selection_distribution_menu == '2': # Если Artix дистрибутив, то
        select_artix_locale_mirrors()

    #CACHYOS
    elif selection_distribution_menu == '3': # Если CachyOS дистрибутив, то
        select_cachyos_locale_mirrors()

    elif selection_distribution_menu.casefold() == 'q':
        exit_logic()


    else:
        os.system('clear')
        console.print('Wrong choice ❌\nTry again')
        console.print('\n\nPress "Enter" to continue ...')
        input()
        selection_distribution()