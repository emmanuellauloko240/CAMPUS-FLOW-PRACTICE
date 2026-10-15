import json


def tickets_report():
    
    open_tickets = 0
    in_progress_ticket = 0
    closed_tickets = 0

    low_priority = 0
    medium_priority = 0
    high_priority = 0
    critical_priority = 0


    with open("tickets.json", "r") as file:
        tickets = json.load(file)
        print("Total Tickets Logged:",len(tickets))
        # print(tickets)
        
        # global open_tickets, in_progress_ticket, closed_tickets
        for ticketDetails in tickets:
            
            if  ticketDetails["status"] == "open":
                open_tickets +=1
            if ticketDetails["status"] == "in progress":
                in_progress_ticket +=1
            if ticketDetails["status"] == "close":
                closed_tickets +=1
            if ticketDetails["priority"] == "low":
                low_priority +=1
            if ticketDetails["priority"] == "medium":
                medium_priority +=1
            if ticketDetails["priority"] == "high":
                high_priority +=1
            if ticketDetails["priority"] == "critical":
                critical_priority +=1

    print("=====================================")
    print("LOGGED TICKET REPORT")
    print("=====================================")
    print("BREAKDOWN BY STATUS")
    print("=====================================")
    print(f"Total Open tickets: {open_tickets}")
    print(f"Total tickets In-progress: {in_progress_ticket}")
    print(f"Total Closed tickets: {closed_tickets}")
    print("=====================================")


    print("=====================================")
    print("BREAKDOWN BY PRIORITY")
    print("=====================================")
    print(f"Total Low priority: {low_priority}")
    print(f"Total Medium priority: {medium_priority}")
    print(f"Total High priority: {high_priority}")
    print(f"Total Critical Priority: {critical_priority}")
    print("=====================================")
        




        
