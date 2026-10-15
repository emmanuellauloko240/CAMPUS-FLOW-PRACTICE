ALLOWED = {
    "open": ["in_progress"],
    "in_progress": ["resolved"],
    "resolved": ["open"],
}

def change_status(tickets, ticket_id,new_status):
    found = None
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            found = ticket
    if found is None:
        raise ValueError("unknown ticket....")
    if new_status not in ALLOWED[found["status"]]:
        raise ValueError ("Invalid status change")
    if new_status == "in_progress" and found["assigned_to"] is None:
        raise ValueError("Ticket must be assigned first")
    found["status"] = new_status
    return found

def assign_ticket(tickets, ticket_id,staff_name):
    found = None
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            found = ticket
            break
    if found is None:
        raise ValueError("unknown ticket....")
    if not isinstance(staff_name, str) or not staff_name.strip():

        raise ValueError ("staff name cannot be blank")

    if found["status"] == "resolved":

        raise ValueError("Resolved ticket cannot be assigned until it is reopened")

    found["assigned_to"] = staff_name.strip()

    return found

PRIORITY_ORDER = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
}

def ticket_sort_key(ticket):
    priority = PRIORITY_ORDER[ticket["priority"]]
    ticket_number = int(ticket["id"][1:])
    return (priority, ticket_number)

def open_work_queue(tickets):
    open_tickets = [t for t in tickets if t["status"] == "open"]
    return sorted(open_tickets, key=ticket_sort_key)
    
