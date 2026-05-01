import os
import sys

from rich.console import Console

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from TUI.info_program import  program_version
from TUI.info_program import last_update

from TUI.all_panels import main_menu_panel, headline_panel

console = Console()


def main_logic():
    os.system('clear')
    headline_panel()
    console.print("\nSelect an action: ")
    main_menu_panel()
    console.print("\nby Costodoston 🥰 | Telegram: https://t.me/Costodoston_Company")
    console.print(f"\n{program_version} | last update: {last_update}")  # program_version - версия программы (файл info)
                                                                        # last_update - последний апдейт программы (файл info)