import subprocess
import re

def get_vm_stat():
    try:
        result = subprocess.run(['vm_stat'], capture_output=True, text=True, check=True)
        return result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        return [f"Error: {e}"]

def extract_value(line):
    match = re.search(r'(\d+)', line.replace('.', ''))
    return int(match.group(1)) if match else 0
