"""Simulated RAM allocation for MiniOS; it does not reserve real RAM."""
TOTAL_MEMORY_MB = 1024

class MemoryManager:
    def __init__(self):
        self.allocations = {}
        self.next_id = 1

    def show(self):
        used = sum(self.allocations.values())
        print("\nMemory Status\n------------------------")
        print(f"Total Memory: {TOTAL_MEMORY_MB} MB\nUsed Memory:  {used} MB\nFree Memory:  {TOTAL_MEMORY_MB-used} MB")
        if self.allocations:
            print("Allocations:")
            for aid, amount in self.allocations.items(): print(f"  ID {aid}: {amount} MB")

    def allocate(self, amount=None):
        if not amount: print("Usage: allocate <MB>"); return
        try: amount = int(amount)
        except ValueError: print("Error: Memory amount must be a whole number."); return
        used = sum(self.allocations.values())
        if amount <= 0: print("Error: Amount must be greater than zero."); return
        if used + amount > TOTAL_MEMORY_MB:
            print(f"Error: Not enough memory. Only {TOTAL_MEMORY_MB-used} MB available."); return
        aid = self.next_id; self.next_id += 1
        self.allocations[aid] = amount
        print(f"{amount} MB allocated. Allocation ID: {aid}")

    def free(self, allocation_id=None):
        if not allocation_id: print("Usage: free <allocation-ID>"); return
        try: aid = int(allocation_id)
        except ValueError: print("Error: Allocation ID must be a number."); return
        amount = self.allocations.pop(aid, None)
        if amount is None: print("Error: Memory allocation ID does not exist."); return
        print(f"{amount} MB released from allocation {aid}.")
