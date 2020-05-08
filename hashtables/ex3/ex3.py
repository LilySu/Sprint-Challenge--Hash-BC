from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        hash_table_resize)

def intersection(arrays):
    """
    YOUR CODE HERE
    """

    hash_dict = {}
    result = []
    for first in arrays[0]:
        hash_dict[first] = 1
    for i in arrays[1:]:
        for after in i:
            if after in hash_dict:
                hash_dict[after] += 1

    result = []
    for i in hash_dict:
        if hash_dict[i] == len(arrays):
            result.append(i)
    return result



if __name__ == "__main__":
    # arrays = []

    # arrays.append(list(range(1000000,2000000)) + [1,2,3])
    # arrays.append(list(range(2000000,3000000)) + [1,2,3])
    # arrays.append(list(range(3000000,4000000)) + [1,2,3])

    # print(intersection(arrays))
    print(intersection([
            [1,2,3],
            [1,4,5],
            [1,6,7]
        ]))