from rich.console import Console
import distro
import locale
import os

from mirrorlist.Arch.Artix.artix_united_kingdom_mirrors import artix_united_kingdom_start
from mirrorlist.Arch.arch_united_kingdom_mirrors import arch_united_kingdom_start
from mirrorlist.Arch.CachyOS.cachyos_russian_mirrors import cachyos_russia_start
from mirrorlist.Arch.Artix.artix_russian_mirrors import artix_russia_start
from mirrorlist.Arch.CachyOS.cachyos_usa_mirrors import cachyos_usa_start
from mirrorlist.Arch.arch_kazakhstan_mirrors import arch_kazakhstan_start
from mirrorlist.Arch.arch_belarus_mirrors import arch_belarus_start
from mirrorlist.Arch.Artix.artix_usa_mirrors import artix_usa_start
from mirrorlist.Arch.arch_ukraine_mirrors import arch_ukraine_start
from mirrorlist.Arch.arch_russian_mirrors import arch_russia_start
from mirrorlist.Arch.arch_usa_mirrors import arch_usa_start
from TUI.exit_logic import exit_logic

console = Console()

def system_verification():
    def name_linux():
        return distro.name()

    def language():
        land = locale.getlocale()
        locale_string = land[0]
        split_locale = locale_string.split('_')[1]
        return split_locale

    verification_language = language()
    verification_distribution = name_linux()

    print(f'\n(Auto) Localization selected: {verification_language}')
    print(f'(Auto) Distribution used: {verification_distribution}\n')

# Arch

    if verification_distribution == 'Arch Linux':

        if verification_language == 'RU':
            arch_russia_start()

        elif verification_language == 'BY':
            arch_belarus_start()

        elif verification_language == 'KZ':
            arch_kazakhstan_start()

        elif verification_language == 'UA':
            arch_ukraine_start()

        elif verification_language == 'US':
            arch_usa_start()

        elif verification_language == 'UK':
            arch_united_kingdom_start()

        elif verification_language == 'US':
            arch_usa_start()

        else:
            error_language()

# CachyOS

    elif verification_distribution == 'CachyOS Linux':

        if verification_language == 'RU':
            cachyos_russia_start()

        elif verification_language == 'US':
            cachyos_usa_start()

        else:
            error_language()

# Artix

    elif verification_distribution == 'Artix Linux':

        if verification_language == 'RU':
           artix_russia_start()

        elif verification_language == 'US':
            artix_usa_start()

        elif verification_language == 'UK':
            artix_united_kingdom_start()

        else:
            error_language()

    else:
        error_distribution()


def error_language():
    os.system('clear')
    console.print('❌ Your localization is not yet supported by the program. Please keep an eye on development.')
    console.print('\n\nPress "Enter" to exit ...')
    input()
    exit_logic()

def error_distribution():
    os.system('clear')
    console.print("❌ Your localization isn't currently supported by the program. Stay tuned for updates.\n\nIt's also possible your region isn't included in the distribution you're using.")
    console.print('\n\nPress "Enter" to exit ...')
    input()
    exit_logic()