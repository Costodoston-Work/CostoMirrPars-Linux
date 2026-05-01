from rich.panel import Panel
from rich import box

from rich.console import Console

console = Console()

# Создаём все панели для навигации в меню

# Отдельная панель с вариантами "Назад" и "Выход"
copy_exit = Panel (
        "[C] Copy mirrors in config\n\n[Q] Exit",
        style="bold white",
        border_style="bold #FFA500",
        box = box.ROUNDED,
        expand = False
)

# Отдельная панель с вариантом "Выход"
exit = Panel (
        "[Q] Exit",
        style="bold white",
        border_style="bold #FFA500",
        box = box.ROUNDED,
        expand = False
)

# Панель главного меню
main_menu = Panel (
        "[A] Auto-Detection\n[M] Manual\n\n[S] Settings\n[I] INFO\n\n[Q] Exit",
        style="bold white",
        border_style="bold #FFA500",
        box = box.ROUNDED,
        expand = False
)

# Панель выбора ветки дистрибутива
manual_menu_distribution_branch = Panel (
        "[1] Arch"
        "\n\n[Q] Exit",
        style="bold white",
        border_style="bold #FFA500",
        box = box.ROUNDED,
        expand = False
)

# ЕСЛИ ВЫБРАНА ARCH ВЕТКА
# Панель выбора дистрибутивов
manual_menu_arch_distribution = Panel (
        "[1] Arch\n[2] Artix\n[3] CachyOS"
        "\n\n[Q] Exit",
        style="bold white",
        border_style="bold #FFA500",
        box = box.ROUNDED,
        expand = False
)

# Панель выбора локализации зеркал, если выбран Arch
manual_menu_locale_distribution_arch = Panel (
        "[1] Russia\n[2] Belarus\n[3] Ukraine\n[4] Kazakhstan\n[5] USA\n[6] United Kingdom"
        "\n\n[Q] Exit",
        style="bold white",
        border_style="bold #FFA500",
        box = box.ROUNDED,
        expand = False
)

# Панель выбора локализации зеркал, если выбран Artix
manual_menu_locale_distribution_artix = Panel (
        "[1] Russia\n[2] USA\n[3] United Kingdom"
        "\n\n[Q] Exit",
        style="bold white",
        border_style="bold #FFA500",
        box = box.ROUNDED,
        expand = False
)

# Панель выбора локализации зеркал, если выбран CachyOS
manual_menu_locale_distribution_cachyos = Panel (
        "[1] Russia\n[2] USA"
        "\n\n[Q] Exit",
        style="bold white",
        border_style="bold #FFA500",
        box = box.ROUNDED,
        expand = False
)

# Заголовок
headline = Panel (
        "CostoMirrPars Utility",
        style="bold #FFA500",
        border_style="bold white",
        box = box.ROUNDED,
        expand = False
)

settings_menu = Panel (
        "[Y] Backup your old mirrors\n\n[Q] Exit",
        style="bold white",
        border_style="bold #FFA500",
        box = box.ROUNDED,
        expand = False
)

info_menu = Panel (
        "[1] INFO file in Russian\n[2] INFO file in English\n\n[Q] Exit",
        style="bold white",
        border_style="bold #FFA500",
        box = box.ROUNDED,
        expand = False
)

def exit_panel():
    console.print(exit)

def main_menu_panel():
    console.print(main_menu)

def manual_menu_locale_distribution_arch_panel():
    console.print(manual_menu_locale_distribution_arch)

def manual_menu_locale_distribution_cachyos_panel():
    console.print(manual_menu_locale_distribution_cachyos)

def manual_menu_arch_distribution_panel():
    console.print(manual_menu_arch_distribution)

def manual_menu_distribution_branch_panel():
    console.print(manual_menu_distribution_branch)

def manual_menu_locale_distribution_artix_panel():
    console.print(manual_menu_locale_distribution_artix)

def headline_panel():
    console.print(headline)

def copy_exit_panel():
        console.print(copy_exit)

def settings_menu_panel():
        console.print(settings_menu)

def info_menu_panel():
        console.print(info_menu)