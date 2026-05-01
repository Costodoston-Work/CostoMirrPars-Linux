import sys
import os

from rich.console import Console

console = Console()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from TUI.exit_logic import exit_logic

from mirrorlist.Arch.Artix.artix_united_kingdom_mirrors import artix_united_kingdom_start
from mirrorlist.Arch.Artix.artix_russian_mirrors import artix_russia_start
from mirrorlist.Arch.Artix.artix_usa_mirrors import artix_usa_start

from mirrorlist.Arch.arch_united_kingdom_mirrors import arch_united_kingdom_start
from mirrorlist.Arch.arch_kazakhstan_mirrors import arch_kazakhstan_start
from mirrorlist.Arch.arch_belarus_mirrors import arch_belarus_start
from mirrorlist.Arch.arch_ukraine_mirrors import arch_ukraine_start
from mirrorlist.Arch.arch_russian_mirrors import arch_russia_start
from mirrorlist.Arch.arch_usa_mirrors import arch_usa_start

from mirrorlist.Arch.CachyOS.cachyos_russian_mirrors import cachyos_russia_start
from mirrorlist.Arch.CachyOS.cachyos_usa_mirrors import cachyos_usa_start

from mirrorlist.paste_mirrors_in_config.copy_arch_mirrors import copy_arch_united_kingdom_mirrors
from mirrorlist.paste_mirrors_in_config.copy_arch_mirrors import copy_arch_kazakhstan_mirrors
from mirrorlist.paste_mirrors_in_config.copy_arch_mirrors import copy_arch_russian_mirrors
from mirrorlist.paste_mirrors_in_config.copy_arch_mirrors import copy_arch_belarus_mirrors
from mirrorlist.paste_mirrors_in_config.copy_arch_mirrors import copy_arch_ukraine_mirrors
from mirrorlist.paste_mirrors_in_config.copy_arch_mirrors import copy_arch_usa_mirrors

from mirrorlist.paste_mirrors_in_config.copy_artix_mirrors import copy_artix_united_kingdom_mirrors
from mirrorlist.paste_mirrors_in_config.copy_artix_mirrors import copy_artix_russian_mirrors
from mirrorlist.paste_mirrors_in_config.copy_artix_mirrors import copy_artix_usa_mirrors

from mirrorlist.paste_mirrors_in_config.copy_cachyos_mirrors import copy_cachyos_russian_mirrors
from mirrorlist.paste_mirrors_in_config.copy_cachyos_mirrors import copy_cachyos_usa_mirrors

from TUI.all_panels import manual_menu_locale_distribution_cachyos_panel
from TUI.all_panels import manual_menu_locale_distribution_artix_panel
from TUI.all_panels import manual_menu_locale_distribution_arch_panel
from TUI.all_panels import copy_exit_panel
from TUI.all_panels import exit_panel
from TUI.all_panels import headline_panel



def select_arch_locale_mirrors():

    #ARCH
    os.system('clear')
    headline_panel()
    console.print('\nSelect mirror location:')
    manual_menu_locale_distribution_arch_panel()  # Список локализации зеркал для выбранного Arch дистрибутива

    selection_locale_distribution_arch = input('\n(selection locale) Выбор: ')
    if selection_locale_distribution_arch == '1': # 1 - Россия
        os.system('clear')
        console.print("# All Russian mirrors:\n", style="#FFA500")
        arch_russia_start()  # Функция парсинга актуальных зеркал
        console.print("")
        copy_exit_panel()

        selection_after_parsing = input('\n(mirrors menu) Choice: ')
        if selection_after_parsing.casefold() == 'q':
            exit_logic()

        elif selection_after_parsing.casefold() == 'c':
            copy_arch_russian_mirrors()
            exit_panel()

            selection_copy_mirrors = input('\n(copy menu) Choice: ')
            if selection_copy_mirrors.casefold() == 'q':
                exit_logic()

        else:
            os.system('clear')
            console.print('Wrong choice ❌\nTry again')
            console.print('\n\nPress "Enter" to continue ...')
            input()
            select_arch_locale_mirrors()

    elif selection_locale_distribution_arch == '2':  # 2 - Беларусь
        os.system('clear')
        console.print("# All Belarus mirrors:\n", style="#FFA500")
        arch_belarus_start()
        console.print("")
        copy_exit_panel()

        selection_after_parsing = input('\n(mirrors menu) Choice: ')
        if selection_after_parsing.casefold() == 'q':
            exit_logic()

        elif selection_after_parsing.casefold() == 'c':
            copy_arch_belarus_mirrors()
            exit_panel()

        else:
            os.system('clear')
            console.print('Wrong choice ❌\nTry again')
            console.print('\n\nPress "Enter" to continue ...')
            input()
            select_arch_locale_mirrors()

            selection_copy_mirrors = input('\n(copy menu) Choice: ')
            if selection_copy_mirrors.casefold() == 'q':
                exit_logic()

    elif selection_locale_distribution_arch == '3':  # 3 - Украина
        os.system('clear')
        console.print("# All Ukraine mirrors:\n", style="#FFA500")
        arch_ukraine_start()
        console.print("")
        copy_exit_panel()
        selection_after_parsing = input('\n(mirrors menu) Choice: ')

        if selection_after_parsing.casefold() == 'q':
            exit_logic()

        elif selection_after_parsing.casefold() == 'c':
            copy_arch_ukraine_mirrors()
            exit_panel()

        else:
            os.system('clear')
            console.print('Wrong choice ❌\nTry again')
            console.print('\n\nPress "Enter" to continue ...')
            input()
            select_arch_locale_mirrors()

            selection_copy_mirrors = input('\n(copy menu) Choice: ')
            if selection_copy_mirrors.casefold() == 'q':
                exit_logic()

    elif selection_locale_distribution_arch == '4':  # 4 - Казахстан
        os.system('clear')
        console.print("# All Kazakhstan mirrors:\n", style="#FFA500")
        arch_kazakhstan_start()
        console.print("")
        copy_exit_panel()

        selection_after_parsing = input('\n(mirrors menu) Choice: ')
        if selection_after_parsing.casefold() == 'q':
            exit_logic()

        elif selection_after_parsing.casefold() == 'c':
            copy_arch_kazakhstan_mirrors()
            exit_panel()

        else:
            os.system('clear')
            console.print('Wrong choice ❌\nTry again')
            console.print('\n\nPress "Enter" to continue ...')
            input()
            select_arch_locale_mirrors()

            selection_copy_mirrors = input('\n(copy menu) Choice: ')
            if selection_copy_mirrors.casefold() == 'q':
                exit_logic()

    elif selection_locale_distribution_arch == '5':  # 5 - США
        os.system('clear')
        console.print("# All USA mirrors:\n", style="#FFA500")
        arch_usa_start()
        console.print("")
        copy_exit_panel()

        selection_after_parsing = input('(mirrors menu) Choice: ')
        if selection_after_parsing.casefold() == 'q':
            exit_logic()

        elif selection_after_parsing.casefold() == 'c':
            copy_arch_usa_mirrors()
            exit_panel()

        else:
            os.system('clear')
            console.print('Wrong choice ❌\nTry again')
            console.print('\n\nPress "Enter" to continue ...')
            input()
            select_arch_locale_mirrors()

            selection_copy_mirrors = input('\n(copy menu) Choice: ')
            if selection_copy_mirrors.casefold() == 'q':
                exit_logic()

    elif selection_locale_distribution_arch == '6':  # 6 - Великобритания
        os.system('clear')
        console.print("# All United Kingdom mirrors:\n", style="#FFA500")
        arch_united_kingdom_start()
        console.print("")
        copy_exit_panel()

        selection_after_parsing = input('(mirrors menu) Choice: ')
        if selection_after_parsing.casefold() == 'q':
            exit_logic()

        elif selection_after_parsing.casefold() == 'c':
            copy_arch_united_kingdom_mirrors()
            exit_panel()

        else:
            os.system('clear')
            console.print('Wrong choice ❌\nTry again')
            console.print('\n\nPress "Enter" to continue ...')
            input()
            select_arch_locale_mirrors()

            selection_copy_mirrors = input('\n(copy menu) Choice: ')
            if selection_copy_mirrors.casefold() == 'q':
                exit_logic()

    elif selection_locale_distribution_arch.casefold() == 'q':
        exit_logic()

    else:
        os.system('clear')
        console.print('Wrong choice ❌\nTry again')
        console.print('\n\nPress "Enter" to continue ...')
        input()
        select_arch_locale_mirrors()


#ARTIX
def select_artix_locale_mirrors():

    os.system('clear')
    headline_panel()
    console.print('\nSelect mirror location:')
    manual_menu_locale_distribution_artix_panel()

    selection_locale_distribution_artix = input('\n(selection locale) Choice: ')

    if selection_locale_distribution_artix == '1': # 1 - Россия
        os.system('clear')
        console.print("# All Russian mirrors:\n", style="#FFA500")
        artix_russia_start()
        console.print("")
        copy_exit_panel()

        if selection_locale_distribution_artix == 'q':
            exit_logic()

        selection_after_parsing = input('\n(mirrors menu) Choice: ')
        if selection_after_parsing.casefold() == 'q':
            exit_logic()

        elif selection_after_parsing.casefold() == 'c':
            copy_artix_russian_mirrors()
            exit_panel()

        else:
            os.system('clear')
            console.print('Wrong choice ❌\nTry again')
            console.print('\n\nPress "Enter" to continue ...')
            input()
            select_artix_locale_mirrors()

            selection_copy_mirrors = input('\n(copy menu) Choice: ')
            if selection_copy_mirrors.casefold() == 'q':
                exit_logic()

    elif selection_locale_distribution_artix == '2':  # 2 - США
        os.system('clear')
        console.print("# All USA mirrors:\n", style="#FFA500")
        artix_usa_start()
        console.print("")
        copy_exit_panel()

        selection_after_parsing = input('\n(mirrors menu) Choice: ')
        if selection_after_parsing.casefold() == 'q':
            exit_logic()

        elif selection_after_parsing.casefold() == 'c':
            copy_artix_usa_mirrors()
            exit_panel()

        else:
            os.system('clear')
            console.print('Wrong choice ❌\nTry again')
            console.print('\n\nPress "Enter" to continue ...')
            input()
            select_artix_locale_mirrors()

            selection_copy_mirrors = input('\n(copy menu) Choice: ')
            if selection_copy_mirrors.casefold() == 'q':
                exit_logic()

    elif selection_locale_distribution_artix == '3':  # 3 - Великобритания
        os.system('clear')
        console.print("# All United Kingdom mirrors:\n", style="#FFA500")
        artix_united_kingdom_start()
        console.print("")
        copy_exit_panel()

        selection_after_parsing = input('\n(mirrors menu) Choice: ')
        if selection_after_parsing.casefold() == 'q':
            exit_logic()

        elif selection_after_parsing.casefold() == 'c':
            copy_artix_united_kingdom_mirrors()
            exit_panel()

        else:
            os.system('clear')
            console.print('Wrong choice ❌\nTry again')
            console.print('\n\nPress "Enter" to continue ...')
            input()
            select_artix_locale_mirrors()

            selection_copy_mirrors = input('\n(copy menu) Choice: ')
            if selection_copy_mirrors.casefold() == 'q':
                exit_logic()

    elif selection_locale_distribution_artix.casefold() == 'q':
        exit_logic()

    else:
        os.system('clear')
        console.print('Wrong choice ❌\nTry again')
        console.print('\n\nPress "Enter" to continue ...')
        input()
        select_artix_locale_mirrors()

#CACHYOS
def select_cachyos_locale_mirrors():

    os.system('clear')
    headline_panel()
    console.print('\nSelect mirror location:')
    manual_menu_locale_distribution_cachyos_panel()
    selection_locale_distribution_cachyos = input('\n(selection locale) Choice: ')

    if selection_locale_distribution_cachyos == '1': # 1 - Россия
        os.system('clear')
        console.print("# All Russian mirrors:\n", style="#FFA500")
        cachyos_russia_start()
        console.print("")
        copy_exit_panel()
        selection_after_parsing = input('\n(mirrors menu) Choice: ')

        if selection_after_parsing.casefold() == 'q':
            exit_logic()

        elif selection_after_parsing.casefold() == 'c':
            copy_cachyos_russian_mirrors()
            exit_panel()

        else:
            os.system('clear')
            console.print('Wrong choice ❌\nTry again')
            console.print('\n\nPress "Enter" to continue ...')
            input()
            select_cachyos_locale_mirrors()

            selection_copy_mirrors = input('\n(copy menu) Choice: ')
            if selection_copy_mirrors.casefold() == 'q':
                exit_logic()

    elif selection_locale_distribution_cachyos == '2':  # 2 - США
        os.system('clear')
        console.print("# All USA mirrors:\n", style="#FFA500")
        cachyos_usa_start()
        console.print("")
        copy_exit_panel()
        selection_after_parsing = input('\n(mirrors menu) Choice: ')

        if selection_after_parsing.casefold() == 'q':
            exit_logic()

        elif selection_after_parsing.casefold() == 'c':
            copy_cachyos_usa_mirrors()
            exit_panel()

        else:
            os.system('clear')
            console.print('Wrong choice ❌\nTry again')
            console.print('\n\nPress "Enter" to continue ...')
            input()
            select_cachyos_locale_mirrors()

            selection_copy_mirrors = input('\n(copy menu) Choice: ')
            if selection_copy_mirrors.casefold() == 'q':
                exit_logic()

    elif selection_locale_distribution_cachyos.casefold() == 'q':
        exit_logic()

    else:
        os.system('clear')
        console.print('Wrong choice ❌\nTry again')
        console.print('\n\nPress "Enter" to continue ...')
        input()
        select_cachyos_locale_mirrors()
