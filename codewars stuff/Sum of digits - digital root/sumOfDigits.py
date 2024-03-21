#URL https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

#Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, 
# continue reducing in this way until a single-digit number is produced. 
# The input will be a non-negative integer.

# Examples:
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def digital_root(n):
    newNum = 0
    run = 0
    nStr = str(n)
    if len(nStr) > 1:
        if run <= 0:
            for num in nStr:
                newNum = newNum + int(num)
                print(newNum)
        if run >= 1:
            str(newNum)

    return newNum
    pass
    # ...


# Solutions/tests
test = 16
answer = 7
if digital_root(test) != answer:
    print(f"Failed test 1 got return {digital_root(test)} should have been {answer}")

test = 942
answer = 6
if digital_root(test) != answer:
    print(f"Failed test 1 got return {digital_root(test)} should have been {answer}")

test = 132189
answer = 6
if digital_root(test) != answer:
    print(f"Failed test 1 got return {digital_root(test)} should have been {answer}")

test = 493193
answer= 2
if digital_root(test) != answer:
    print(f"Failed test 1 got return {digital_root(test)} should have been {answer}")