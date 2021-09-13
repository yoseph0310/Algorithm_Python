tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]


def sol(tickets):
    answer = []
    tickets.sort()
    used_ticket = []
    DFS(tickets, "ICN", used_ticket)

    answer = ["ICN"]
    for ticket_num in used_ticket:
        answer.append(tickets[ticket_num][1])
    return answer

def DFS(tickets, start, used_ticket):
    for i in range(len(tickets)):
        if tickets[i][0] == start and i not in used_ticket:
            used_ticket.append(i)
            DFS(tickets, tickets[i][1], used_ticket)

            if len(used_ticket) == len(tickets):
                return
            else:
                used_ticket.pop()

print(sol(tickets))