import unittest
from ticket import create_ticket
from workflow import change_status


class TestWorkflow(unittest.TestCase):
    def make(self):
        tickets = []
        t = create_ticket(tickets, "Wi-Fi down", "Network", "high", 15)
        return tickets, t

    def test_cannot_start_unassigned_ticket(self):
        tickets, t = self.make()
        with self.assertRaises(ValueError):
            change_status(tickets, t["id"], "in_progress")
        self.assertEqual(t["status"], "open")

    def test_cannot_skip_open_to_resolved(self):
        tickets, t = self.make()
        with self.assertRaises(ValueError):
            change_status(tickets, t["id"], "resolved")
        self.assertEqual(t["status"], "open")

    def test_full_path_open_to_resolved(self):
        tickets, t = self.make()
        t["assigned_to"] = "Amina"
        change_status(tickets, t["id"], "in_progress")
        change_status(tickets, t["id"], "resolved")
        self.assertEqual(t["status"], "resolved")

    def test_reopen_resolved_ticket(self):
        tickets, t = self.make()
        t["assigned_to"] = "Amina"
        change_status(tickets, t["id"], "in_progress")
        change_status(tickets, t["id"], "resolved")
        change_status(tickets, t["id"], "open")
        self.assertEqual(t["status"], "open")

    def test_resolved_cannot_go_to_in_progress(self):
        tickets, t = self.make()
        t["assigned_to"] = "Amina"
        change_status(tickets, t["id"], "in_progress")
        change_status(tickets, t["id"], "resolved")
        with self.assertRaises(ValueError):
            change_status(tickets, t["id"], "in_progress")
        self.assertEqual(t["status"], "resolved")

    def test_unknown_ticket_is_rejected(self):
        tickets, t = self.make()
        with self.assertRaises(ValueError):
            change_status(tickets, "T999", "in_progress")


if __name__ == "__main__":
    unittest.main()