tickets = []
luckyTickets = 0
for number in range(1, 1000000):
    if len(str(number)) < 6:
        difference = 6 - len(str(number))
        zeroes = '0' * difference
        ticket = zeroes + str(number)
        tickets.append(ticket)
    else:
        tickets.append(str(number))
for ticket in tickets:
    if int(ticket[0]) + int(ticket[1]) + int(ticket[2]) == int(ticket[3]) + int(ticket[4]) + int(ticket[5]):
        luckyTickets += 1
print('There are ' + str(luckyTickets) + ' lucky tickets')
