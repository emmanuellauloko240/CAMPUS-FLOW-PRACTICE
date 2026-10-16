import json
import os

ALLOWED_CATEGORIES = ["Network", "Hardware", "Software", "Other"]
ALLOWED_URGENCIES = ["low", "medium", "high"]

def main_main():
    filename = "tickets.json"

    # Load existing tickets before creating new ones
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        storedtickets = []
    else:
        with open(filename, "r") as file:
            storedtickets = json.load(file)

    # Work with the existing tickets
    tickets = storedtickets

    while True:
        create_ticket_from_input(tickets)

        again = input("Create another? (y/n): ")

        if again.strip().lower() != "y":
            break

    print("Tickets created:", len(tickets))
    print(tickets)

    # Save all tickets
    with open(filename, "w") as file:
        json.dump(tickets, file, indent=4)

    print("Tickets saved successfully")

def calculate_priority(urgency, affected_users):
    if urgency == "high" and affected_users >= 10:
        return "critical"
    elif urgency == "high" or affected_users >= 10:
        return "high"
    elif urgency == "medium" or affected_users >= 3:
        return "medium"
    else:
        return "low"


def ticket(ticket_id, title, category, urgency, affected_users):
    title = title.strip()
    category = category.strip().capitalize()
    urgency = urgency.strip().lower()

    if title == "":
        raise ValueError("Title cannot be blank")

    if category not in ALLOWED_CATEGORIES:
        raise ValueError("Invalid category")

    if urgency not in ALLOWED_URGENCIES:
        raise ValueError("Invalid urgency")

    if (
        not isinstance(affected_users, int)
        or isinstance(affected_users, bool)
        or affected_users <= 0
    ):
        raise ValueError("Affected users must be a positive whole number")

    priority = calculate_priority(urgency, affected_users)

    fellow = {
        "id": ticket_id,
        "title": title,
        "affected_users": affected_users,
        "category": category,
        "urgency": urgency,
        "status": "open",
        "assigned_to": None,
        "priority": priority
    }

    return fellow


def next_id(tickets):
    # Find the highest existing ticket number
    highest_number = 0

    for existing_ticket in tickets:
        ticket_id = existing_ticket.get("id", "")

        if ticket_id.startswith("T") and ticket_id[1:].isdigit():
            number = int(ticket_id[1:])
            highest_number = max(highest_number, number)

    return f"T{highest_number + 1:03}"


def create_ticket(tickets, title, category, urgency, affected_users):
    new_id = next_id(tickets)

    new = ticket(new_id, title, category, urgency, affected_users)

    tickets.append(new)

    return new


def create_ticket_from_input(tickets):
    title = input("Title: ")
    category = input("Category (Network/Hardware/Software): ")
    urgency = input("Urgency (low/medium/high): ")
    users_text = input("Affected users: ")

    try:
        affected_users = int(users_text)

        new = create_ticket(
            tickets,
            title,
            category,
            urgency,
            affected_users
        )

        print("Created", new["id"], "- priority:", new["priority"])

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()