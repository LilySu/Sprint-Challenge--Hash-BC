from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    ht = HashTable(16)# size 16
    for i in range(len(weights)):
        index = weights[i]
        is_equal = hash_table_retrieve(ht, limit - index)
        if is_equal is not None:
            return (i, is_equal)      
        else:
            hash_table_insert(ht, index, i)
    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")