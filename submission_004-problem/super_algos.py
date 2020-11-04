
def find_min(element):
    """TODO: complete for Step 1"""
    '''
    The function is to find the minimum integer in a list. It also checks if there are no 
    characters in the list, if so it returns -1
    '''
    x = element
    for i in element:
        if isinstance(i,int) == False:
            return -1
    if len(x) == 1:
        return x[0]
    if len(x) == 0 :
        return -1
    if x[1] > x[0]:
        x.append(x[0])
        return(find_min(element[1:]))
    else:
        return(find_min(element[1:]))




def sum_all(element):
    """TODO: complete for Step 2"""
    '''
    The function is to sum up all the integers in a list and if there are 
    any characters in the list it returns -1
    '''

    for i in element:
        if isinstance(i,int) == False:
            return -1
    if len(element) == 1:
        return(element[0])
    elif len(element) == 0:
        return -1
    else:
        return element[0] + sum_all(element[1:])


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    '''
    This funtion checks for char in the set/list and returns an
    empty list if so. It also calls the function character_combo and stores 
    the value in a list and returns that list
    '''
    result = []
    #prefix = []
    for char in character_set:
        if type(char) != str:
            return []
    length = len(character_set)
    character_combo(character_set, n, result, "", length)
    return result
    
def character_combo(character_set, n, result, prefix, length):
    '''
    This function creates the different patterns and is called by find_possible_strings.
    It also calls the result and uses the stored value to create a new list
    '''
    if n == 0:
        result.append(prefix)
        return result
    for x in range(length):
        new_set = prefix + character_set[x]
        character_combo(character_set,n-1 ,result, new_set, length)

#print(find_possible_strings(["a", "b", "c"], 3))
        


