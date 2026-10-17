"""Sandboxed simulated file management for MiniOS."""
from pathlib import Path

class FileSystem:
    def __init__(self, workspace: Path):
        self.workspace = workspace.resolve()
        self.workspace.mkdir(parents=True, exist_ok=True)
        self.current_dir = self.workspace

    def safe_path(self, name):
        if not name:
            raise ValueError("Please provide a file or directory name.")
        path = (self.current_dir / name).resolve()
        if path != self.workspace and self.workspace not in path.parents:
            raise ValueError("Access denied: paths must stay inside the MiniOS workspace.")
        return path

    def relative_path(self):
        try:
            return str(self.current_dir.relative_to(self.workspace)) or "/"
        except ValueError:
            return "/"

    def pwd(self):
        print(self.current_dir)

    def dir(self, name=None):
        path = self.safe_path(name) if name else self.current_dir
        if not path.exists():
            print("Error: Directory does not exist."); return
        if not path.is_dir():
            print("Error: That path is not a directory."); return
        print(f"\nDirectory of {self.relative_path() if path == self.current_dir else path.name}")
        entries = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
        if not entries: print("(empty)")
        for item in entries:
            print(f"{'<DIR> ' if item.is_dir() else '      '} {item.name}")

    def mkdir(self, name=None):
        if not name: print("Usage: mkdir <directory-name>"); return
        path = self.safe_path(name); path.mkdir()
        print(f"Directory created: {name}")

    def create(self, filename=None):
        if not filename: print("Usage: create <filename>"); return
        path = self.safe_path(filename)
        if path.exists(): print("Error: A file or directory with that name already exists."); return
        path.touch(); print(f"File created: {filename}")

    def read(self, filename=None):
        if not filename: print("Usage: read <filename>"); return
        path = self.safe_path(filename)
        if not path.is_file(): print("Error: File does not exist."); return
        print(path.read_text(encoding="utf-8"))

    def write(self, filename=None, *content):
        if not filename or not content: print('Usage: write <filename> "text to save"'); return
        path = self.safe_path(filename)
        if path.exists() and not path.is_file(): print("Error: That path is a directory."); return
        path.write_text(" ".join(content), encoding="utf-8")
        print(f"Content saved to {filename}.")

    def delete(self, filename=None):
        if not filename: print("Usage: delete <filename>"); return
        path = self.safe_path(filename)
        if not path.is_file(): print("Error: File does not exist."); return
        path.unlink(); print(f"File deleted: {filename}")

    def rename(self, old=None, new=None):
        if not old or not new: print("Usage: rename <old-name> <new-name>"); return
        source, target = self.safe_path(old), self.safe_path(new)
        if not source.exists(): print("Error: Source does not exist."); return
        if target.exists(): print("Error: Destination already exists."); return
        source.rename(target); print(f"Renamed '{old}' to '{new}'.")

    def cd(self, folder=None):
        if not folder or folder == ".": return
        target = (self.current_dir / ".." if folder == ".." else self.safe_path(folder)).resolve()
        if target != self.workspace and self.workspace not in target.parents:
            print("Error: Cannot leave the MiniOS workspace."); return
        if not target.is_dir(): print("Error: Directory does not exist."); return
        self.current_dir = target
