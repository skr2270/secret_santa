import random
from typing import List, Dict, Tuple
from models.employee import Employee

MAX_RETRIES = 100

class SecretSantaAssigner:
    def __init__(self, employees: List[Employee], previous_assignments: Dict[Tuple[str, str], Tuple[str, str]]):
        self.employees = employees
        self.previous_assignments = previous_assignments
        self.assignments = {}

    def assign_secret_children(self) -> Dict[Employee, Employee]:
        for _ in range(MAX_RETRIES):
            try:
                return self._try_assign()
            except ValueError:
                continue
        raise Exception("Failed to assign Secret Santa without violating constraints.")

    def _try_assign(self) -> Dict[Employee, Employee]:
        assignments = {}
        available = set(self.employees)
        shuffled = self.employees.copy()
        random.shuffle(shuffled)

        for giver in shuffled:
            options = list(available - {giver})

            # Remove last year's assignee if exists
            prev_child_info = self.previous_assignments.get((giver.name, giver.email))
            if prev_child_info:
                options = [e for e in options if (e.name, e.email) != prev_child_info]

            if not options:
                raise ValueError(f"No valid assignment for {giver.name} ({giver.email})")

            chosen = random.choice(options)
            assignments[giver] = chosen
            available.remove(chosen)

        self.assignments = assignments
        return assignments
