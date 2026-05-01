import distro
import locale

from mirrorlist.paste_mirrors_in_config.copy_arch_mirrors import copy_arch_russian_mirrors, copy_arch_belarus_mirrors, \
    copy_arch_kazakhstan_mirrors, copy_arch_ukraine_mirrors, copy_arch_usa_mirrors, copy_arch_united_kingdom_mirrors
from mirrorlist.paste_mirrors_in_config.copy_artix_mirrors import copy_artix_usa_mirrors, copy_artix_russian_mirrors, \
    copy_artix_united_kingdom_mirrors
from mirrorlist.paste_mirrors_in_config.copy_cachyos_mirrors import copy_cachyos_usa_mirrors, \
    copy_cachyos_russian_mirrors


def logic_for_copy_all_mirrors_in_configs():
    def name_linux():
        return distro.name()

    def language():
        land = locale.getlocale()
        locale_string = land[0]
        split_locale = locale_string.split('_')[1]
        return split_locale

    verification_language = language()
    verification_distribution = name_linux()


# Arch

    if verification_distribution == 'Arch Linux':

        if verification_language == 'RU':
            copy_arch_russian_mirrors()

        if verification_language == 'BY':
            copy_arch_belarus_mirrors()

        if verification_language == 'KZ':
            copy_arch_kazakhstan_mirrors()

        if verification_language == 'UA':
            copy_arch_ukraine_mirrors()

        if verification_language == 'US':
            copy_arch_usa_mirrors()

        if verification_language == 'GB':
            copy_arch_united_kingdom_mirrors()


# CachyOS

    if verification_distribution == 'CachyOS Linux':

        if verification_language == 'RU':
            copy_cachyos_russian_mirrors()

        if verification_language == 'US':
            copy_cachyos_usa_mirrors()

# Artix

    if verification_distribution == 'Artix Linux':

        if verification_language == 'RU':
            copy_artix_russian_mirrors()

        if verification_language == 'US':
            copy_artix_usa_mirrors()

        if verification_language == 'GB':
            copy_artix_united_kingdom_mirrors()