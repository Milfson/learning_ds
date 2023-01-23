import numpy as np
count = 0
lst_num = lst_num = list(range(101))
def binary_search_recursive(lst_num = lst_num, start = lst_num[0], end = lst_num[-1], number:int=np.random.randint(1, 101)):
    global count
    count += 1
    if start > end:
        return -1

    mid = (start + end) // 2
    if number == lst_num[mid]:
        return count

    if number < lst_num[mid]:
        return binary_search_recursive(lst_num, start, mid-1, number)
    else:
        return binary_search_recursive(lst_num, mid+1, end, number)
print(binary_search_recursive())
            

