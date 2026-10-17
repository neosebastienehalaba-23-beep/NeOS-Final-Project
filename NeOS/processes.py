"""Simulated process management; does not launch Windows processes."""
class ProcessManager:
    def __init__(self):
        self.processes = {}
        self.next_pid = 1

    def list_processes(self):
        print("PID   NAME                 STATUS")
        if not self.processes:
            print("No running simulated processes."); return
        for pid, proc in self.processes.items():
            print(f"{pid:<5} {proc['name']:<20} {proc['status']}")

    def run(self, name=None):
        if not name: print("Usage: run <program-name>"); return
        pid = self.next_pid; self.next_pid += 1
        self.processes[pid] = {"name": name, "status": "RUNNING"}
        print(f"Process started.\nPID: {pid}\nName: {name}\nStatus: RUNNING")

    def kill(self, pid=None):
        if not pid: print("Usage: kill <PID>"); return
        try: pid_num = int(pid)
        except ValueError: print("Error: PID must be a number."); return
        proc = self.processes.pop(pid_num, None)
        if proc is None: print("Error: Process does not exist."); return
        print(f"Process {pid_num} ({proc['name']}) terminated.")
