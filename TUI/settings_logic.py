import os
import shutil
import distro

from TUI.exit_logic import exit_logic
from  rich.console import Console

from TUI.all_panels import settings_menu_panel, headline_panel

console = Console()

def name_linux():
    return distro.name()

verification_distribution = name_linux()

def settings_logic():
    os.system('clear')
    headline_panel()
    console.print("\nSelect an action: ")
    settings_menu_panel()
    selection_settings_menu = input('\n(settings menu) Choice: ')

    if selection_settings_menu.casefold() == 'y':

        if not os.path.exists('BACKUP_YOUR_OLD_MIRRORS'):
            os.mkdir('BACKUP_YOUR_OLD_MIRRORS')

        if verification_distribution == 'Arch Linux' or 'Artix Linux' or 'CachyOS Linux':
            shutil.copy('/etc/pacman.d/mirrorlist', './BACKUP_YOUR_OLD_MIRRORS')
            shutil.copy('/etc/pacman.d/cachyos-v3-mirrorlist', './BACKUP_YOUR_OLD_MIRRORS')
            shutil.copy('/etc/pacman.d/cachyos-v4-mirrorlist', './BACKUP_YOUR_OLD_MIRRORS')

            console.print('\nOld mirrors have been successfully copied in folder "BACKUP_YOUR_OLD_MIRRORS" ✅')
            console.print('\n\nPress "Enter" to continue ...')
            input()
            settings_logic()

    elif selection_settings_menu.casefold() == 'q':
        exit_logic()


    else:
        os.system('clear')
        console.print('Wrong choice ❌\nTry again')
        console.print('\n\nPress "Enter" to continue ...')
        input()
        settings_logic()