import copy
import unittest

from workflow import assign_ticket, open_work_queue, change_status


def make(ticket_id, priority="low", status="open", assigned_to=None):
    return {
        "id": ticket_id,
        "title": f"Ticket {ticket_id}",
        "category": "Other",
        "urgency": "low",
        "affected_users": 1,
        "priority": priority,
        "status": status,
        "assigned_to": assigned_to,
    }


class TestAssign(unittest.TestCase):
    def test_assign_sets_trimmed_name(self):
        tickets = [make("T001")]
        assign_ticket(tickets, "T001", "  Staff A ")
        self.assertEqual(tickets[0]["assigned_to"], "Staff A")

    def test_blank_name_rejected_and_nothing_changes(self):
        tickets = [make("T001")]
        before = copy.deepcopy(tickets)
        with self.assertRaises(ValueError):
            assign_ticket(tickets, "T001", "   ")
        self.assertEqual(tickets, before)

    def test_unknown_ticket_rejected_and_nothing_changes(self):
        tickets = [make("T001")]
        before = copy.deepcopy(tickets)
        with self.assertRaises(ValueError):
            assign_ticket(tickets, "T999", "Staff A")
        self.assertEqual(tickets, before)

    def test_resolved_ticket_cannot_be_assigned(self):
        tickets = [make("T001", status="resolved", assigned_to="Staff A")]
        before = copy.deepcopy(tickets)
        with self.assertRaises(ValueError):
            assign_ticket(tickets, "T001", "Staff B")
        self.assertEqual(tickets, before)

    def test_assigned_ticket_can_now_start(self):
        tickets = [make("T001")]
        assign_ticket(tickets, "T001", "Staff A")
        change_status(tickets, "T001", "in_progress")
        self.assertEqual(tickets[0]["status"], "in_progress")


class TestOpenWorkQueue(unittest.TestCase):
    def ids(self, tickets):
        return [t["id"] for t in open_work_queue(tickets)]

    def test_only_open_tickets_appear(self):
        tickets = [
            make("T001", "critical", "open"),
            make("T002", "critical", "in_progress", "Staff A"),
            make("T003", "critical", "resolved", "Staff A"),
        ]
        self.assertEqual(self.ids(tickets), ["T001"])

    def test_priority_order_critical_to_low(self):
        tickets = [
            make("T001", "low"),
            make("T002", "medium"),
            make("T003", "critical"),
            make("T004", "high"),
        ]
        self.assertEqual(self.ids(tickets), ["T003", "T004", "T002", "T001"])

    def test_ties_use_numeric_id_not_text(self):
        # As text, "T10" sorts before "T2". As numbers, 2 comes before 10.
        tickets = [make("T10", "high"), make("T2", "high")]
        self.assertEqual(self.ids(tickets), ["T2", "T10"])

    def test_queue_does_not_change_tickets(self):
        tickets = [make("T002", "low"), make("T001", "high")]
        before = copy.deepcopy(tickets)
        open_work_queue(tickets)
        self.assertEqual(tickets, before)

    def test_empty_list_gives_empty_queue(self):
        self.assertEqual(open_work_queue([]), [])


if __name__ == "__main__":
    unittest.main()
