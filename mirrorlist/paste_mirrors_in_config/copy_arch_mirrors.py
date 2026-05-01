from mirrorlist.Arch.arch_united_kingdom_mirrors import arch_united_kingdom_start
from mirrorlist.Arch.arch_kazakhstan_mirrors import arch_kazakhstan_start
from mirrorlist.Arch.arch_ukraine_mirrors import arch_ukraine_start
from mirrorlist.Arch.arch_belarus_mirrors import arch_belarus_start
from mirrorlist.Arch.arch_russian_mirrors import arch_russia_start
from mirrorlist.Arch.arch_usa_mirrors import arch_usa_start

from TUI.all_panels import headline_panel

from rich.console import Console

import pyperclip
import os

console = Console()

def copy_arch_russian_mirrors():
    russia_all_mirrors = arch_russia_start()
    if russia_all_mirrors:
        all_mirrors_text = '\n'.join(russia_all_mirrors)
        pyperclip.copy(all_mirrors_text)
        os.system('clear')
        headline_panel()
        console.print('\nCopied to clipboard:\n', style="bold #FFA500")

        paste = all_mirrors_text.replace('"', '\\"').replace('$', '\\$')
        os.system(f'echo "{paste}" | sudo tee /etc/pacman.d/mirrorlist')
        console.print('\n\nMirrors added in /etc/pacman.d/mirrorlist', style="bold #FFA500")


def copy_arch_belarus_mirrors():
    belarus_all_mirrors = arch_belarus_start()
    if belarus_all_mirrors:
        all_mirrors_text = '\n'.join(belarus_all_mirrors)
        pyperclip.copy(all_mirrors_text)
        os.system('clear')
        headline_panel()
        console.print('\nCopied to clipboard:\n', style="bold #FFA500")

        paste = all_mirrors_text.replace('"', '\\"').replace('$', '\\$')
        os.system(f'echo "{paste}" | sudo tee /etc/pacman.d/mirrorlist')
        console.print('\n\nMirrors added in /etc/pacman.d/mirrorlist', style="bold #FFA500")


def copy_arch_kazakhstan_mirrors():
    kazakhstan_all_mirrors = arch_kazakhstan_start()
    if kazakhstan_all_mirrors:
        all_mirrors_text = '\n'.join(kazakhstan_all_mirrors)
        pyperclip.copy(all_mirrors_text)
        os.system('clear')
        headline_panel()
        console.print('\nCopied to clipboard:\n', style="bold #FFA500")

        paste = all_mirrors_text.replace('"', '\\"').replace('$', '\\$')
        os.system(f'echo "{paste}" | sudo tee /etc/pacman.d/mirrorlist')
        console.print('\n\nMirrors added in /etc/pacman.d/mirrorlist', style="bold #FFA500")


def copy_arch_united_kingdom_mirrors():
    united_kingdom_all_mirrors = arch_united_kingdom_start()
    if united_kingdom_all_mirrors:
        # Копируем ВСЕ зеркала в буфер
        all_mirrors_text = '\n'.join(united_kingdom_all_mirrors)
        pyperclip.copy(all_mirrors_text)
        os.system('clear')
        headline_panel()
        console.print('\nCopied to clipboard:\n', style="bold #FFA500")

        paste = all_mirrors_text.replace('"', '\\"').replace('$', '\\$')
        os.system(f'echo "{paste}" | sudo tee /etc/pacman.d/mirrorlist')
        #Записываем ВСЕ зеркала в файл
        console.print('\n\nMirrors added in /etc/pacman.d/mirrorlist', style="bold #FFA500")


def copy_arch_usa_mirrors():
    usa_all_mirrors = arch_usa_start()
    if usa_all_mirrors:
        all_mirrors_text = '\n'.join(usa_all_mirrors)
        pyperclip.copy(all_mirrors_text)
        os.system('clear')
        headline_panel()
        console.print('\nCopied to clipboard:\n', style="bold #FFA500")

        paste = all_mirrors_text.replace('"', '\\"').replace('$', '\\$')
        os.system(f'echo "{paste}" | sudo tee /etc/pacman.d/mirrorlist')
        console.print('\n\nMirrors added in /etc/pacman.d/mirrorlist', style="bold #FFA500")

def copy_arch_ukraine_mirrors():
    ukraine_all_mirrors = arch_ukraine_start()
    if ukraine_all_mirrors:
        all_mirrors_text = '\n'.join(ukraine_all_mirrors)
        pyperclip.copy(all_mirrors_text)
        os.system('clear')
        headline_panel()
        console.print('\nCopied to clipboard:\n', style="bold #FFA500")

        paste = all_mirrors_text.replace('"', '\\"').replace('$', '\\$')
        os.system(f'echo "{paste}" | sudo tee /etc/pacman.d/mirrorlist')
        console.print('\n\nMirrors added in /etc/pacman.d/mirrorlist', style="bold #FFA500")