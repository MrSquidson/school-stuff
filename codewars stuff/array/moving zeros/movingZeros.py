# URL: https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

'''Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]'''

def move_zeros(lst):
    returnList = []
    zeros = 0
    if lst == []: #If list is empty just return it right away
        return lst
    
    while lst.index(0) > 1:
        lst.remove(lst.index(0))
        zeros += 1
    while zeros > 0:
        lst.append(0)
        zeros -= 1

    '''for elm in lst:
        if elm == 0:
            lst.pop()
            zeros += 1
        if elm != 0:
            returnList.append(elm)
    while zeros > 0:
        returnList.append(0)
        zeros -= 1'''
    return lst


# Tests
failures = 0
lst = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1] 
answer = [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
if move_zeros(lst) != answer:
    print(f"Failed test 1 got return {move_zeros(lst)} should have been {answer}")
    failures += 1
else:
    print(f'Passed test 1 with response {move_zeros(lst)}')

lst = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
answer = [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if move_zeros(lst) != answer:
    print(f"Failed test 2 got return {move_zeros(lst)} should have been {answer}")
    failures += 1
else:
    print(f'Passed test 2 with response {move_zeros(lst)}')

lst = [0, 0]
answer = [0, 0]
if move_zeros(lst) != answer:
    print(f"Failed test 3 got return {move_zeros(lst)} should have been {answer}")
    failures += 1
else:
    print(f'Passed test 3 with response {move_zeros(lst)}')

lst = [0] 
answer = [0]
if move_zeros(lst) != answer:
    print(f"Failed test 4 got return {move_zeros(lst)} should have been {answer}")
    failures += 1
else:
    print(f'Passed test 4 with response {move_zeros(lst)}')

lst = []
answer = []
if move_zeros(lst) != answer:
    print(f"Failed test 5 got return {move_zeros(lst)} should have been {answer}")
    failures += 1
else:
    print(f'Passed test 5 with response {move_zeros(lst)}')

print(f"{failures} out of 5 tests failed!")