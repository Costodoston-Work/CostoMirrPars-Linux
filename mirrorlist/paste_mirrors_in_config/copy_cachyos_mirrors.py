from mirrorlist.Arch.CachyOS.cachyos_russian_mirrors import cachyos_russia_start
from mirrorlist.Arch.CachyOS.cachyos_usa_mirrors import cachyos_usa_start

from rich.console import Console

from TUI.all_panels import headline_panel

import pyperclip
import os

console = Console()

def copy_cachyos_russian_mirrors():
    russia_all_mirrors = cachyos_russia_start()
    if russia_all_mirrors:
        all_mirrors_text = '\n'.join(russia_all_mirrors)
        pyperclip.copy(all_mirrors_text)
        os.system('clear')
        headline_panel()
        console.print('\nCopied to clipboard:\n', style="bold #FFA500")

        paste = all_mirrors_text.replace('"', '\\"').replace('$', '\\$')
        os.system(f'echo "{paste}" | sudo tee /etc/pacman.d/cachyos-mirrorlist sudo tee /etc/pacman.d/cachyos-v3-mirrorlist sudo tee /etc/pacman.d/cachyos-v4-mirrorlist')

        console.print("\n\nMirrors added in /etc/pacman.d/cachyos-mirrorlist ; /etc/pacman.d/cachyos-v3-mirrorlist ; /etc/pacman.d/cachyos-v4-mirrorlist", style="bold #FFA500")


def copy_cachyos_usa_mirrors():
    usa_all_mirrors = cachyos_usa_start()
    if usa_all_mirrors:
        all_mirrors_text = '\n'.join(usa_all_mirrors)
        pyperclip.copy(all_mirrors_text)
        os.system('clear')
        headline_panel()
        console.print('\nCopied to clipboard:\n', style="bold #FFA500")

        paste = all_mirrors_text.replace('"', '\\"').replace('$', '\\$')
        os.system(f'echo "{paste}" | sudo tee /etc/pacman.d/cachyos-mirrorlist sudo tee /etc/pacman.d/cachyos-v3-mirrorlist sudo tee /etc/pacman.d/cachyos-v4-mirrorlist')

        console.print('\n\nMirrors added in /etc/pacman.d/cachyos-mirrorlist ; /etc/pacman.d/cachyos-v3-mirrorlist ; /etc/pacman.d/cachyos-v4-mirrorlist', style="bold #FFA500")
