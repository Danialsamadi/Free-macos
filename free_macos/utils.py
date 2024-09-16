import signal
import sys
import subprocess
from rich.console import Console

console = Console()

def handle_exit(signum, frame):
    subprocess.run("clear", shell=True)
    console.print("[bold red]Exiting...[/bold red]")
    sys.exit(0)

def setup_signal_handlers():
    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)
