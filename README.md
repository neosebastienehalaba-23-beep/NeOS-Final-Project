# MiniOS NeOS v2.0

## Project Name

**MiniOS NeOS** — a simple command-line operating system simulator developed for the Operating Systems final project.

## Group Members

1. Neo Sebastiene C. Halaba
2. Kody Benz O. Reyes
3. Paul Nazarene S. Jordan
4. Daphnie Claire A. Montalban
5. Kym Niecoole R. Jabican
6. Aaron John Demakiling

## Project Description

MiniOS NeOS is a Python-based command-line program that simulates selected functions of a basic operating system. Users can sign in, manage files and directories in a dedicated workspace, start and terminate simulated processes, and allocate or release simulated memory. It also displays basic system information and handles invalid commands. MiniOS is an educational simulator; it is not a real or bootable operating system and does not manage actual Windows processes or physical RAM.

## Features

- Command-line interface with a `MiniOS` prompt that displays the current user and directory
- Help menu with command descriptions and examples
- User login with demo `admin` and `student` accounts
- User listing and logout/sign-in flow
- File and directory management
- Simulated process management with process IDs (PIDs)
- Simulated memory allocation and release
- System information display
- Date, time, command history, and uptime commands
- Error handling for unknown commands, invalid arguments, and common file/process/memory errors
- Clean shutdown using `exit`

## Project Structure

```text
MiniOS/
├── main.py
├── README.md
├── requirements.txt
├── users.py
├── filesystem.py
├── processes.py
└── memory.py
```

- `main.py` — starts MiniOS and routes user commands
- `users.py` — handles demo user authentication and listing
- `filesystem.py` — manages the MiniOS file workspace
- `processes.py` — simulates process creation, listing, and termination
- `memory.py` — simulates memory allocation and release

## Requirements

- Python 3.9 or newer
- Windows Command Prompt (CMD); PowerShell or another terminal may also work
- No third-party Python packages are required

## How to Run

1. Clone the repository or download and extract the project ZIP file.
2. Open Windows Command Prompt (CMD).
3. Navigate to the project folder. For example:

   ```cmd
   cd path\to\MiniOS
   ```

4. Start MiniOS:

   ```cmd
   python main.py
   ```

5. Sign in using one of the demo accounts:

   | Username | Password |
   |---|---|
   | `admin` | `admin123` |
   | `student` | `student123` |

6. Type `help` to display the commands available in the simulator.

## Available Commands

Commands that require an argument are shown with the argument in angle brackets. Do not type the angle brackets themselves.

### General and User Commands

| Command | Description |
|---|---|
| `help` | Displays the available commands and examples. |
| `clear` | Clears the terminal screen. |
| `date` | Displays the current date. |
| `time` | Displays the current time. |
| `whoami` | Displays the currently logged-in user. |
| `users` | Lists the available user accounts. |
| `login` | Displays a message explaining the sign-in flow. |
| `logout` | Signs out the current user and returns to the login prompt. |
| `history` | Shows commands entered during the current session. |
| `uptime` | Displays how long MiniOS has been running. |
| `systeminfo` | Displays MiniOS version, architecture, simulated CPU and memory, and current user. |
| `exit` | Shuts down MiniOS. |

### File Management Commands

| Command | Description |
|---|---|
| `dir` or `ls` | Lists files and directories in the current location. |
| `mkdir <name>` | Creates a directory. |
| `create <file>` or `touch <file>` | Creates an empty file. |
| `read <file>` or `cat <file>` | Displays a file's contents. |
| `write <file> <text>` | Writes text to a file. Put text containing spaces in quotation marks. |
| `delete <file>` or `rm <file>` | Deletes a file. |
| `rename <old> <new>` | Renames a file or directory. |
| `cd <folder>` | Changes the current directory. Use `cd ..` to move to the parent directory. |
| `pwd` | Displays the current MiniOS directory. |

### Process Management Commands

| Command | Description |
|---|---|
| `process` or `ps` | Lists simulated processes. |
| `run <program-name>` | Starts a simulated process and assigns it a PID. |
| `kill <PID>` | Terminates a simulated process using its PID. |

### Memory Management Commands

| Command | Description |
|---|---|
| `memory` | Displays total, used, and free simulated memory. |
| `allocate <MB>` | Allocates the specified amount of simulated memory in megabytes. |
| `free <allocation-ID>` | Releases a previous allocation using its allocation ID. |

## Example Session

```text
mkdir Documents
cd Documents
create notes.txt
write notes.txt "Operating Systems Final Project"
read notes.txt
cd ..
run calculator
process
kill 1
allocate 200
memory
free 1
systeminfo
exit
```

## Notes and Limitations

- Files created with MiniOS are stored in the automatically created `mini_os_files/` directory beside the Python files.
- Demo user accounts are saved in an automatically created `users.json` file.
- Process and memory information are simulations and reset when the program exits.
- Demo passwords are stored as plain text and should only be used for classroom demonstrations.
