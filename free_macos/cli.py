import click
import time
import threading
from rich.live import Live
from rich.console import Console

from .core import get_vm_stat
from .progress import create_progress_table
from .ignore_input import ignore_keyboard_input


console = Console()


@click.command()
@click.option('--interval', default=1, help='Time interval (in seconds) between refreshes')
def show_vm_stat(interval):
    max_value = 1000000

    input_thread = threading.Thread(target=ignore_keyboard_input, daemon=True)
    input_thread.start()

    live = Live(console=console, refresh_per_second=1)
    with live:
        while True:
            vm_stat_lines = get_vm_stat()
            progress, tasks = create_progress_table(vm_stat_lines, max_value)

            live.update(progress)

            for task, pages in tasks:
                progress.update(task, completed=pages)

            time.sleep(interval)


if __name__ == '__main__':
    show_vm_stat()
