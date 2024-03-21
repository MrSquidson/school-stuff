# URL: https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/train/python
# When provided with a number between 0-9, return it in words.
# Input :: 1
# Output :: "One".
# If your language supports it, try using a switch statement.

import random
def switch_it_up(number):
    word = ["Zero", "One", "Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    return word[number]

print(switch_it_up(random.randint(0,9)))
