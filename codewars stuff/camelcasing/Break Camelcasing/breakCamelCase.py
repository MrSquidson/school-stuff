# URL: https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
# Complete the solution so that the function will break up camel casing, using a space between words.

# Examples:

# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    position = 0
    for char in s:
        if char.isUpper() == True:

        
    pass


# Tests
s = "camelCasing"
if solution(s) == "camel Casing": print('Works!')
else: print(f"Didn't work returned {solution(s)}")

s = "identifier"
if solution(s) == "identifier": print('Works!')
else: print(f"Didn't work returned {solution(s)}")

s = ""
if solution(s) == "": print('Works!')
else: print(f"Didn't work returned {solution(s)}")