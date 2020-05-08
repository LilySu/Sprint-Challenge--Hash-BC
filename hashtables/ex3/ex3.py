from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        hash_table_resize)

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    arrays = sorted(arrays, key=lambda x: len(x))
    hash_dict = {}
    result = []
    for first in arrays[0]:
        hash_dict[first] = 1
    for i in arrays[1:]:
        for after in i:
            if after in hash_dict:
                hash_dict[after] += 1
    # new_list = []
    # for i in hash_dict:
    #     if hash_dict[i] == len(arrays):
    #         new_list.append(i)
    result = []
    for i in hash_dict:
        if hash_dict[i] == len(arrays):
            result.append(i)
    return result
    # for i in range(len(arrays)):
    #     if hash_dict[i] == len(arrays):
    #         result = i
    # # result = [num for num in hash_dict if hash_dict[num] == len(arrays)]
    #         return result



    # for i in arrays:
    #     length = len(arrays)
    #     hashtable = HashTable(length)
    #     new = [None] * length

    # # Initialize an empty hashtable
    # # Iterate through the first array and put every element of the first array in the hashtable
    # for i in range(len(arrays)):
    #     hash_table_insert(hashtable, i, arrays[i])

    # for j in arrays:
    #     new = hash_table_retrieve(hashtable, i)

    # for i in new:
    #     # if i in arrays:
    #     print([list(filter(lambda x: i in new, sublist)) for sublist in arrays])
            
    
    # for j in range(len(arrays)):
    #     value = hash_table_retrieve(hashtable, i)
    #     if value in 
    #     print(hash_table_retrieve(hashtable, i))
    # for i in new:
    #     print(new.values)
    
    # for j in range(len(arrays)):
    #     if 
    #     repeat = hash_table_retrieve(hashtable, i)
    #     if repeat is not None:
    #         return repeat
    # return None


    # # # For every element x of the next array
    # for j in range(len(arrays)):    
    #     # Search x in the set hashtable. If x is present, then print it.
    # #     new[j] = hash_table_retrieve(hashtable, new[j])
    # # return new
    #     print(new[j])
    # print(new)


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