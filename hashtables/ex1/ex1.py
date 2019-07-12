#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # Base case, should terminate if there is less than 2 weights
    if len(weights) <= 1:
        return None

    #Initiate a result and a hash table
    result = []
    table = {}

    # Loop over the weights, figure out the sum minus the weight
    for i in range(0, len(weights)):
        limit_minus_weight = limit - weights[i]

        table[weights[i]] = limit_minus_weight

    for i in range(0, len(weights)):
        if limit - weights[i] in table:
            result.insert(0, i)

    return result


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)
