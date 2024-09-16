# Free-macos

Have you ever wanted to use the `free` command on macOS? Now you can! The Free macOS project gives you the ability to monitor your system’s memory status with real-time updates and visual progress bars.

But wait, this isn’t just about commands. It’s a live activity monitor for your memory status, implemented with colorful progress bars to give you a clear view of your system’s memory usage.

![Free-macos](https://github.com/user-attachments/assets/7a99d7b1-2330-4555-a723-3be0a98a590d)


## Features

- **Live Memory Monitoring:** Visualize memory usage with progress bars.
- **Real-time Updates:** Get up-to-date information about your system’s memory status.
- **Customizable Refresh Interval:** Adjust the interval time between updates using the `--interval` option.
- **Formatted Output:** Memory values are displayed in B, KB, MB, or GB.
- **Easy Setup:** Quickly set up and run the monitoring tool.

## Installation

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```sh
   git clone https://github.com/Danialsamadi/Free-macos.git

2. **Navigate to the Project Directory**

   ```sh
   cd Free-macos
   ```

3. **Install Dependencies**

   Use Poetry to install the project dependencies:

   ```sh
   poetry install
   ```
   
## Usage

### Running with Poetry

To run the Free macOS project using Poetry, navigate to the project directory and use the following command:

```sh
poetry run free --interval 2
```

This example sets the refresh interval to 2 seconds. Adjust the interval as needed to suit your preferences.

### Set Up an Alias

To simplify running the project, you can set up an alias in your shell configuration.

Add the following alias to your `.zshrc` or `.bashrc` file, replacing `/path/to/your/project` with the actual path to your project directory:

```sh
alias free="cd /path/to/your/project && poetry run free"
```

After adding the alias, reload your shell configuration:

```sh
source ~/.zshrc
# or
source ~/.bashrc
```

Now you can use the `free` command from anywhere in your terminal to monitor your memory status.

## Contributing

If you want to contribute to the project, feel free to submit a pull request or open an issue. We welcome contributions and feedback!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
