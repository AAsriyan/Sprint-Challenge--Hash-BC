#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    #insert the tickets into the hash table
    for i in range(length):
        hash_table_insert(ht, tickets[i].source, tickets[i].destination)

    # Setting the first destination to starting point's destination
    route[0] = hash_table_retrieve(ht, 'NONE')

    # After we have our starting point, we loop through the route list and set the next destination in the list
    for i in range(1, length):
        route[i] = hash_table_retrieve(ht, route[i-1])

    # Return the list of routes as the answer
    return route

reconstruct_trip([
  Ticket("PIT", "ORD"),
  Ticket("XNA", "CID"),
  Ticket("SFO", "BHM"),
  Ticket("FLG", "XNA"),
  Ticket("NONE", "LAX"),
  Ticket("LAX", "SFO"),
  Ticket("CID", "SLC"),
  Ticket("ORD", "NONE"),
  Ticket("SLC", "PIT"),
  Ticket("BHM", "FLG")
], 10)