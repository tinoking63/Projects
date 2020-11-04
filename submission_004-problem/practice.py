# def find_min(element):
#     x = element
#     for i in element:
#         if isinstance(i,int) == False:
#             return -1
#     if len(x) == 1:
#         return x[0]
#     if len(x) == 0 :
#         return -1
#     if x[1] > x[0]:
#         x.append(x[0])
#         return(find_min(element[1:]))
#     else:
#         return(find_min(element[1:]))

# print(find_min([124,124,12,4]))

# print(find_min(["12"]))

# def sum_all(element):
#     total = 0
#     print(type(element))
#     # if len(element) == 1:
#     #     return(element[0])
#     # elif len(element) == 0:
#     #     return -1
#     # else:
#     #     return element[0] + sum_all(element[1:])
#     total1 = element[0] + element[1]
#     element.pop(0)
#     element.append(total1)
#     return sum_all(element[0])
#     print(total)
#     print(element)

#     # if len(element) == 1:
#     #     return element[0]
#     # if element[0] == "":
#     #     return -1
#     # else:
#     #     total = element[0] + element[1]
#     #     element.pop()
#     #     element.append(element[0])
#     # return sum_all(element[1:])


# print(sum_all([2,3,5]))

def find_all_possible_strings(character_sets,n):
    result = []
    #prefix = []
    for char in character_sets:
        if type(char) != str:
            return []
    length = len(character_sets)
    character_combo(character_sets, n, result, "", length)
    return result

def character_combo(character_sets, n, result, prefix, length):
    if n == 0:
        result.append(prefix)
        return result
    for x in range(length):
        new_set = prefix + character_sets[x]
        character_combo(character_sets,n-1 ,result, new_set, length)
    
    
    #for x in character_combo(prefix,(n-1)):
    #for x in character_combo(character_sets, n - 1):
    # for x in character_sets:
    #     if char in character_sets:
    #         result.append(prefix[0] + x + char)
    #         print('result:', result)
    # return(character_combo(character_sets, n - 1))


print('char combo', find_all_possible_strings(('a','b'),3))