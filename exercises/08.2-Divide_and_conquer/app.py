list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(list_of_items):

    odd = []
    even = []

    for item in list_of_items:
        if (item % 2) == 0:
            # print("{0} is Even".format(item))
            even.append(item)
            # print(even)
        else:
            odd.append(item)   
            # print(odd)
    # for item in even:
        # odd.append(item)
    new_list = []
    new_list.append(odd)  
    
    new_list.append(even)
    return new_list

        

    


print(merge_two_list(list_of_numbers))

        

        





