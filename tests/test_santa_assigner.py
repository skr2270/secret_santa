import unittest
from models.employee import Employee
from services.santa_assigner import SecretSantaAssigner

class TestSecretSantaAssigner(unittest.TestCase):
    def test_no_self_assignment_or_repeat(self):
        emp1 = Employee("A", "a@acme.com")
        emp2 = Employee("B", "b@acme.com")
        emp3 = Employee("C", "c@acme.com")

        employees = [emp1, emp2, emp3]
        previous = {
            ("A", "a@acme.com"): ("B", "b@acme.com"),
            ("B", "b@acme.com"): ("C", "c@acme.com"),
            ("C", "c@acme.com"): ("A", "a@acme.com"),
        }

        assigner = SecretSantaAssigner(employees, previous)
        assignments = assigner.assign_secret_children()

        for giver, receiver in assignments.items():
            self.assertNotEqual(giver, receiver)
            self.assertNotEqual((receiver.name, receiver.email), previous.get((giver.name, giver.email)))

    def test_failure_on_single_employee(self):
        employees = [Employee("Solo", "solo@acme.com")]
        assigner = SecretSantaAssigner(employees, {})
        with self.assertRaises(Exception):
            assigner.assign_secret_children()

if __name__ == '__main__':
    unittest.main()