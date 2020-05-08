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
    for i in arrays[0]:# for each item in the first list of array
        hash_dict[i] = 1 # insert into dictionary set key to 1
    for listitem in arrays[1:]:# for each item thereafter
        for i in listitem:
            if i in hash_dict:
                hash_dict[i] += 1

    result = []
    for i in hash_dict:# for each item in dictionary
        if hash_dict[i] == len(arrays): # if value is equal to the length of the array
            result.append(i) # append to result
    return result




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