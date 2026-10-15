# from storage import list_and_view
# from report import tickets_report
# from workflow import change_status
# from ticket import main_main


# def main():
#     while True:
#         print("\nSelect an option:")
#         print("F1 - CREATE: Create a new ticket")
#         print("F2 - LIST / VIEW: View tickets")
#         print("F3 - ASSIGN: Assign a ticket")
#         print("F4 - WORKFLOW: Change ticket status")
#         print("F5 - WORK QUEUE: View unresolved tickets")
#         print("F6 - REPORTS: View ticket reports")
#         print("F7 - PERSISTENCE: Save and load tickets")
#         print("Q - QUIT")

#         user_select = input("Select an option: ").strip().upper()

#         if user_select == "F1":
#             main_main()
#         elif user_select == "F2":
#             list_and_view()
#         elif user_select == "F3":
#             print("Assignment feature is not implemented yet.")
#         elif user_select == "F4":
#             change_status()
#         elif user_select == "F5":
#             print("Work queue feature is not implemented yet.")
#         elif user_select == "F6":
#             tickets_report()
#         elif user_select == "F7":
#             print("Persistence feature is not implemented yet.")
#         elif user_select == "Q":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid option. Please try again.")


# if __name__ == "__main__":
#     main()

import json

from storage import list_and_view
from report import tickets_report
from workflow import change_status, assign_ticket, open_work_queue
from ticket import main_main

DATA_FILE = "tickets.json"


def load_tickets_safely():
    """Return the list of tickets, [] if the file is missing, or None if the
    file is unreadable (so we never overwrite data we could not read)."""
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: tickets.json is not valid JSON. Nothing was changed.")
        return None
    if not isinstance(data, list):
        print("Error: tickets.json has an unexpected format. Nothing was changed.")
        return None
    return data


def save_tickets_safely(tickets):
    with open(DATA_FILE, "w") as file:
        json.dump(tickets, file, indent=2)


def Assign_from_input():
    tickets = load_tickets_safely()
    if tickets is None:
        return
    ticket_id = input("Ticket ID to assign: ").strip().upper()
    staff_name = input("Assign to (staff name): ")
    try:
        assign_ticket(tickets, ticket_id, staff_name)
    except ValueError as error:
        print(f"Could not assign: {error}")
        return
    save_tickets_safely(tickets)
    print(f"{ticket_id} Assigned to {staff_name.strip()}")


def change_status_from_input():
    tickets = load_tickets_safely()
    if tickets is None:
        return
    ticket_id = input("Ticket ID: ").strip().upper()
    new_status = input("New status (in_progress / resolved / open): ").strip().lower()
    try:
        change_status(tickets, ticket_id, new_status)
    except ValueError as error:
        print(f"Could not change status: {error}")
        return
    save_tickets_safely(tickets)
    print(f"{ticket_id} is now {new_status}")


def show_work_queue():
    tickets = load_tickets_safely()
    if tickets is None:
        return
    queue = open_work_queue(tickets)
    if not queue:
        print("No open tickets.")
        return
    print("===================================")
    print("OPEN WORK QUEUE")
    print("===================================")
    for ticket in queue:
        print(f"{ticket['id']}  {ticket['priority']:<8}  {ticket['title']}")
    print("===================================")


def main():
    while True:
        print("\nSelect an option:")
        print("F1 - CREATE: Create a new ticket")
        print("F2 - LIST / VIEW: View tickets")
        print("F3 - ASSIGN: Assign a ticket")
        print("F4 - WORKFLOW: Change ticket status")
        print("F5 - WORK QUEUE: View open tickets")
        print("F6 - REPORTS: View ticket reports")
        print("F7 - PERSISTENCE: Save and load tickets")
        print("Q - QUIT")

        user_select = input("Select an option: ").strip().upper()

        if user_select == "F1":
            main_main()
        elif user_select == "F2":
            list_and_view()
        elif user_select == "F3":
            Assign_from_input()
        elif user_select == "F4":
            change_status_from_input()
        elif user_select == "F5":
            show_work_queue()
        elif user_select == "F6":
            tickets_report()
        elif user_select == "F7":
            print("Persistence feature is not implemented yet.")
        elif user_select == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()