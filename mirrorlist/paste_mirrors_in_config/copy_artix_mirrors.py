from mirrorlist.Arch.Artix.artix_united_kingdom_mirrors import artix_united_kingdom_start
from mirrorlist.Arch.Artix.artix_russian_mirrors import artix_russia_start
from mirrorlist.Arch.Artix.artix_usa_mirrors import artix_usa_start

from rich.console import Console

from TUI.all_panels import headline_panel

import pyperclip
import os

console = Console()

def copy_artix_russian_mirrors():
    russia_all_mirrors = artix_russia_start()
    if russia_all_mirrors:
        all_mirrors_text = '\n'.join(russia_all_mirrors)
        pyperclip.copy(all_mirrors_text)
        os.system('clear')
        console.print('\nCopied to clipboard:\n', style="bold #FFA500")

        paste = all_mirrors_text.replace('"', '\\"').replace('$', '\\$')
        os.system(f'echo "{paste}" | sudo tee /etc/pacman.d/mirrorlist')
        console.print('\n\nMirrors added in /etc/pacman.d/mirrorlist', style="bold #FFA500")


def copy_artix_united_kingdom_mirrors():
    united_kingdom_all_mirrors = artix_united_kingdom_start()
    if united_kingdom_all_mirrors:
        # Копируем ВСЕ зеркала в буфер
        all_mirrors_text = '\n'.join(united_kingdom_all_mirrors)
        pyperclip.copy(all_mirrors_text)
        os.system('clear')
        console.print('\nCopied to clipboard:\n', style="bold #FFA500")

        paste = all_mirrors_text.replace('"', '\\"').replace('$', '\\$')
        os.system(f'echo "{paste}" | sudo tee /etc/pacman.d/mirrorlist')
        #Записываем ВСЕ зеркала в файл
        console.print('\n\nMirrors added in /etc/pacman.d/mirrorlist', style="bold #FFA500")


def copy_artix_usa_mirrors():
    usa_all_mirrors = artix_usa_start()
    if usa_all_mirrors:
        all_mirrors_text = '\n'.join(usa_all_mirrors)
        pyperclip.copy(all_mirrors_text)
        headline_panel()
        os.system('clear')
        console.print('\nCopied to clipboard:\n', style="bold #FFA500")

        paste = all_mirrors_text.replace('"', '\\"').replace('$', '\\$')
        os.system(f'echo "{paste}" | sudo tee /etc/pacman.d/cachyos-mirrorlist')
        console.print('\n\nMirrors added in /etc/pacman.d/cachyos-mirrorlist', style="bold #FFA500")



