import json

def list_and_view():
    with open("tickets.json", "r") as file:
        tickets = json.load(file)
        
    print("===================================")
    print("ID    Ticket Title")
    print("===================================")


    for x in tickets:
        
        print(x["id"], x["title"])
    print("===================================")
    print("please enter specific ticket ID to view more details")        
    print("===================================")
    viewticket = input("Enter ticket ID to view: ")
    checkticket = viewticket

    for ticketDetails in tickets:
        # print(checkticket, "and seen", ticketDetails )
        if checkticket == ticketDetails["id"]:
            print("Found")
            print(ticketDetails)
        

    

