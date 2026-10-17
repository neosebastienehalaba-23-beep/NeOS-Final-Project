"""Demo user account and login management for Mini OS."""
import getpass
import json
from pathlib import Path

DEFAULT_USERS = {"admin": "admin123", "student": "student123"}

class UserManager:
    def __init__(self, users_file: Path):
        self.users_file = users_file
        self.users = dict(DEFAULT_USERS)
        try:
            if users_file.exists():
                loaded = json.loads(users_file.read_text(encoding="utf-8") or "{}")
                if isinstance(loaded, dict):
                    self.users.update({str(k): str(v) for k, v in loaded.items()})
        except (OSError, json.JSONDecodeError) as exc:
            print(f"Warning: Could not load user accounts: {exc}")
        self.save()

    def save(self):
        try:
            self.users_file.write_text(json.dumps(self.users, indent=2), encoding="utf-8")
        except OSError as exc:
            print(f"Warning: Could not save user accounts: {exc}")

    def authenticate(self):
        print("\n" + "=" * 42 + "\n              MiniOS Login\n" + "=" * 42)
        print("Demo accounts: admin / admin123  |  student / student123")
        while True:
            try:
                username = input("Username: ").strip()
                password = getpass.getpass("Password: ")
            except (EOFError, KeyboardInterrupt):
                print("\nLogin cancelled.")
                return None
            if self.users.get(username) == password:
                print(f"\nLogin successful. Welcome, {username}!\n")
                return username
            print("Invalid username or password. Please try again.\n")

    def list_users(self):
        print("Registered users:")
        for username in sorted(self.users):
            print(f"- {username}")
