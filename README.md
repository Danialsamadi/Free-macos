
# Free-macOS

> Bring the power of Linux's `free` command to macOS with real-time visual memory monitoring

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab.svg)](https://www.python.org/)
[![Poetry](https://img.shields.io/badge/Poetry-dependency%20management-60a5fa.svg)](https://python-poetry.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![macOS](https://img.shields.io/badge/macOS-compatible-000000.svg)](https://www.apple.com/macos/)

Ever missed the `free` command on macOS? **Free-macOS** brings it back—and makes it better. Monitor your system's memory in real-time with colorful progress bars and live statistics, right in your terminal.

![Free-macos Demo](https://github.com/user-attachments/assets/7a99d7b1-2330-4555-a723-3be0a98a590d)

## ✨ Why Free-macOS?

macOS doesn't include the beloved `free` command that Linux users rely on. Free-macOS fills that gap and enhances it with:

- 📊 **Visual Progress Bars** - See memory usage at a glance with colorful indicators
- ⚡ **Real-Time Updates** - Live monitoring with customizable refresh intervals
- 🎨 **Beautiful Output** - Clean, formatted display with automatic unit conversion (B/KB/MB/GB)
- 🔧 **Zero Configuration** - Works out of the box with sensible defaults
- 🚀 **Lightweight** - Minimal resource footprint

## 🎯 Features

| Feature | Description |
|---------|-------------|
| **Live Monitoring** | Continuous memory status updates in your terminal |
| **Progress Bars** | Visual representation of memory usage (Used, Free, Active, Wired, Compressed) |
| **Custom Intervals** | Adjust refresh rate with `--interval` flag |
| **Smart Formatting** | Automatic unit conversion for readability |
| **Easy Integration** | Set up as a system-wide command with simple aliasing |

## 📦 Installation

### Prerequisites
- macOS (10.14+)
- Python 3.8 or higher
- Poetry (for dependency management)

### Quick Setup

```bash
# 1. Clone the repository
git clone https://github.com/Danialsamadi/Free-macos.git
cd Free-macos

# 2. Install dependencies with Poetry
poetry install

# 3. Run the tool
poetry run free --interval 2
```

That's it! You're now monitoring your system's memory.

## 🚀 Usage

### Basic Usage

Run with default settings (1-second refresh):
```bash
poetry run free
```

### Custom Refresh Interval

Set your preferred update frequency (in seconds):
```bash
poetry run free --interval 2    # Updates every 2 seconds
poetry run free --interval 0.5  # Updates every 500ms (fast)
poetry run free --interval 5    # Updates every 5 seconds (slow)
```

### Global Command Setup

Make `free` available system-wide by adding an alias to your shell configuration:

**For Zsh (default on modern macOS):**
```bash
# Add to ~/.zshrc
echo 'alias free="cd /path/to/Free-macos && poetry run free"' >> ~/.zshrc
source ~/.zshrc
```

**For Bash:**
```bash
# Add to ~/.bashrc or ~/.bash_profile
echo 'alias free="cd /path/to/Free-macos && poetry run free"' >> ~/.bashrc
source ~/.bashrc
```

> 💡 **Pro Tip:** Replace `/path/to/Free-macos` with your actual project path. Use `pwd` in the project directory to get the full path.

Now run `free` from anywhere in your terminal! 🎉

## 📊 Understanding the Output

Free-macOS displays the following memory metrics:

- **Total** - Total physical RAM installed
- **Used** - Memory currently in use by applications
- **Free** - Completely unused memory
- **Active** - Recently used memory that's still in RAM
- **Wired** - Memory required by the system (cannot be compressed or paged out)
- **Compressed** - Memory that's been compressed to save space

Progress bars show the percentage of each metric relative to total memory.

## 🛠️ Development

### Project Structure
```
Free-macos/
├── free_macos/          # Main source code
│   ├── __init__.py
│   └── main.py          # Core monitoring logic
├── pyproject.toml       # Poetry configuration
├── poetry.lock          # Locked dependencies
└── README.md
```

### Adding Features

Want to enhance Free-macOS? Here are some ideas:
- Export metrics to CSV/JSON
- Add alerts for high memory usage
- Historical memory graphs
- Swap memory monitoring
- Process-level memory breakdown

## 🤝 Contributing

Contributions are welcome! Whether it's bug fixes, new features, or documentation improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Issues

Found a bug or have a feature request? [Open an issue](https://github.com/Danialsamadi/Free-macos/issues) on GitHub.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the classic Linux `free` command
- Built for macOS users who miss their Linux tools
- Thanks to the Python and Poetry communities

## 📧 Contact

**Danial Samadi** - [@Danialsamadi](https://github.com/Danialsamadi)

Project Link: [https://github.com/Danialsamadi/Free-macos](https://github.com/Danialsamadi/Free-macos)

---

⭐ If Free-macOS makes your life easier, give it a star!

