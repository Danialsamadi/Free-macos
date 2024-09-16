from rich.progress import Progress, BarColumn, TextColumn
from .core import extract_value

def format_size(pages):
    bytes_size = pages * 16384
    if bytes_size < 1024:
        return f"{bytes_size} B"
    elif bytes_size < 1024 ** 2:
        return f"{bytes_size / 1024:.2f} KB"
    elif bytes_size < 1024 ** 3:
        return f"{bytes_size / (1024 ** 2):.2f} MB"
    else:
        return f"{bytes_size / (1024 ** 3):.2f} GB"

def create_progress_table(vm_stat_lines, max_value):
    progress = Progress(
        TextColumn("[bold blue]{task.description}"),
        BarColumn(bar_width=None, complete_style="bold green", finished_style="bold cyan", pulse_style="bold red"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}% | Size: {task.fields[size]}"),
        refresh_per_second=10
    )

    tasks = []
    excluded_lines = ["Pages throttled"]

    for line in vm_stat_lines:
        if any(excluded in line for excluded in excluded_lines) or "Mach Virtual Memory Statistics" in line or "page size of" in line:
            continue

        pages = extract_value(line)
        task = progress.add_task(description=line, total=max_value, size=format_size(pages))
        tasks.append((task, pages))

    return progress, tasks
