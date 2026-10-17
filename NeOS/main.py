"""Mini OS NeOS v2.0 - command-line operating system simulator."""
from datetime import datetime
from pathlib import Path
import os
import shlex
import sys
import time

from users import UserManager
from filesystem import FileSystem
from processes import ProcessManager
from memory import MemoryManager, TOTAL_MEMORY_MB

APP_NAME = "Mini OS NeOS"
VERSION = "2.0"
BASE_DIR = Path(__file__).resolve().parent

class MiniOS:
    def __init__(self):
        self.running = True
        self.start_time = time.time()
        self.current_user = None
        self.command_history = []
        self.users = UserManager(BASE_DIR / "users.json")
        self.files = FileSystem(BASE_DIR / "mini_os_files")
        self.process_manager = ProcessManager()
        self.memory_manager = MemoryManager()
        self.commands = {
            "help": self.help, "clear": self.clear, "date": self.show_date,
            "time": self.show_time, "whoami": self.whoami, "users": self.users.list_users,
            "login": self.login_command, "logout": self.logout, "history": self.history,
            "uptime": self.uptime, "systeminfo": self.systeminfo, "exit": self.exit,
            "dir": self.files.dir, "ls": self.files.dir, "mkdir": self.files.mkdir,
            "create": self.files.create, "touch": self.files.create, "read": self.files.read,
            "cat": self.files.read, "write": self.files.write, "delete": self.files.delete,
            "rm": self.files.delete, "rename": self.files.rename, "cd": self.files.cd,
            "pwd": self.files.pwd, "process": self.process_manager.list_processes,
            "ps": self.process_manager.list_processes, "run": self.process_manager.run,
            "kill": self.process_manager.kill, "memory": self.memory_manager.show,
            "allocate": self.memory_manager.allocate, "free": self.memory_manager.free,
        }

    def login(self):
        self.current_user = self.users.authenticate()
        if self.current_user is None: self.running = False

    def run(self):
        print("=" * 42 + f"\n       {APP_NAME.upper()} v{VERSION}\n" + "=" * 42)
        print("Welcome! Type 'help' to view available commands.")
        self.login()
        while self.running:
            try:
                raw = input(f"{self.current_user}@MiniOS:{self.files.relative_path()}> ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nUse 'exit' to shut down MiniOS."); continue
            if not raw: continue
            try: parts = [p.strip('"') for p in shlex.split(raw, posix=False)]
            except ValueError as exc:
                print(f"Input error: {exc}"); continue
            self.command_history.append(raw)
            command, *args = parts
            func = self.commands.get(command.lower())
            if func is None:
                print("Unknown command. Type 'help' to see available commands."); continue
            try: func(*args)
            except TypeError: print(f"Invalid arguments for '{command}'. Type 'help' for usage.")
            except (OSError, ValueError) as exc: print(f"Error: {exc}")

    def help(self, *args):
        print("""
AVAILABLE COMMANDS
General:          help, clear, date, time, whoami, users, login, logout, history, uptime, systeminfo, exit
File management:  dir, mkdir <name>, create <file>, read <file>, write <file> <text>, delete <file>, rename <old> <new>, cd <folder>, pwd
Processes:        process, run <program-name>, kill <PID>
Memory:           memory, allocate <MB>, free <allocation-ID>

Examples:
  mkdir Documents
  create notes.txt
  write notes.txt "Operating Systems Final Project"
  read notes.txt
  run calculator
  allocate 200

Aliases: ls=dir, touch=create, cat=read, rm=delete, ps=process
Files are stored in the mini_os_files folder beside this program.
""")

    def clear(self, *args): os.system("cls" if os.name == "nt" else "clear")
    def show_date(self, *args): print(datetime.now().strftime("Date: %Y-%m-%d"))
    def show_time(self, *args): print(datetime.now().strftime("Time: %H:%M:%S"))
    def whoami(self, *args): print(f"Current User: {self.current_user or 'none'}")
    def systeminfo(self, *args):
        print("\n" + "=" * 40 + "\n          SYSTEM INFORMATION\n" + "=" * 40)
        print(f"OS Name: {APP_NAME}\nVersion: {VERSION}\nArchitecture: {64 if sys.maxsize > 2**32 else 32}-bit")
        print(f"CPU: Simulated Virtual CPU\nMemory: {TOTAL_MEMORY_MB} MB\nUser: {self.current_user}")
        print("File workspace: mini_os_files\n" + "=" * 40)
    def login_command(self, *args): print("Use 'logout' to sign out and sign in again.")
    def logout(self, *args):
        if not self.current_user: print("No user is currently logged in."); return
        print(f"Logged out {self.current_user}.")
        self.login()
    def history(self, *args):
        if not self.command_history: print("No commands entered yet."); return
        for i, command in enumerate(self.command_history, 1): print(f"{i:>3}. {command}")
    def uptime(self, *args):
        seconds = int(time.time() - self.start_time)
        hours, rem = divmod(seconds, 3600); minutes, seconds = divmod(rem, 60)
        print(f"System Uptime: {hours}h {minutes}m {seconds}s")
    def exit(self, *args):
        self.running = False
        print("Shutting down Mini OS...\nGoodbye!")

if __name__ == "__main__":
    try: MiniOS().run()
    except KeyboardInterrupt: print("\nMini OS interrupted. Goodbye!")
