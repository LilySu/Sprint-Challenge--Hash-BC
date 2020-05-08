from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        # the `source` string represents the starting airport and the 
        self.destination = destination
        # `destination` string represents the next airport along our trip.

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    """
    The ticket for your first flight has a destination with a `source` of
    `NONE`, and the ticket for your final flight has a `source` with a
    `destination` of `NONE`. 
    Pseudocode for an array of `Tickets` might look like this:
    ```
    tickets = [
    Ticket{ source: "PIT", destination: "ORD" },
    """
    for i in range(len(tickets)):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    route[0] = hash_table_retrieve(hashtable, 'NONE')

    for j in range(1, len(tickets)):
        route[j] = hash_table_retrieve(hashtable, route[j - 1])
    # route.pop()

    return route
