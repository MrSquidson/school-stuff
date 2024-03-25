# URL: https://www.codewars.com/kata/65c0161a2380ae78052e5731/train/python
'''Note: Based off Minecraft, hopefully you at least know the game!

Story: You want to create a giant mine shaft, but you're a little stingy with your iron and diamonds and would not mine out all of the stone with iron or diamond pickaxes. Instead, you rely on less durable but cheaper stone pickaxes! You will need a lot of stone pickaxes though as they break faster than diamond or iron ones, so you need to find out how many stone pickaxes you can craft before you run out of sticks and cobblestones. Unfortunately, you're not an organized person, and you leave all of your materials in a single chest with random junk that you need to filter.

Task: Given an array, return the maximum amount of stone pickaxes you can craft before you run out of sticks and cobblestones. Within the array would be a series of strings with the exact names of the materials listed below. A single stone pickaxe is made of 3 "Cobblestone" and 2 "Sticks", check if your given array contains enough "Sticks" and "Cobblestone" to craft a single stone pickaxe or even more. Do not count any materials apart from "Cobblestones", "Sticks" and "Wood". Wood can be converted into 4 sticks!

Here are the materials you would expect in an array:

Sticks
Cobblestone
Stone (These are different from cobblestone and cannot be used to make a stone pickaxe.)
Wool
Dirt
Wood (Can be treated as sticks, typically 4 sticks for 1 wood)
Diamond

Array sizes are randomized and range from 1 - 200 with randomized contents.

Examples:

Array: ["Sticks", "Sticks", "Cobblestone", "Cobblestone", "Cobblestone"]
Returned: 1

Array: ["Wood", "Cobblestone", "Cobblestone", "Cobblestone"]
Returned: 1

Array: []
Returned: 0

Array: ["Sticks", "Wool", "Cobblestone"]
Returned: 0

Array: ["Cobblestone", "Cobblestone", "Cobblestone", "Cobblestone", "Cobblestone", "Cobblestone", "Wood"]
Returned: 2

Good Luck :D

Made by miggycoder, this is my first kata I ever created.
'''

arr = (["Sticks"]*4 + ["Cobblestone"]*3) # Opens an array containing 4 strings containing the word "Stick" and 3 strings containing the word "Cobblestone"

def stone_pick(arr): # Function named stone_pick running with the array 'arr' as a variable 
    cobble = 0 # Opens cobble variable as the intiger 0
    sticks = 0
    stone_pick = 0
    
    for items in arr: # For every 'items'/instance in the array 'arr'
        match items: # tries to match items with cases
            case 'Cobblestone': # i.e. if it's named 'cobblestone'
                cobble += 1
                pass

            case 'Sticks':
                sticks += 1
                pass

            case 'Wood': # Wood is worth 4 sticks
                sticks += 4
                pass

            case _: #If it doesn't match the above cases
                # Yeah these dont matter
                pass

    while cobble >= 3: # While the 'cobble' variable is more than or equal to 3 
        if sticks >= 2: # and if the variable sticks is more than or equal to 2
            sticks -= 2 #remove 2 sticks
            cobble -= 3 #remove 3 cobble
            stone_pick += 1 #add stone pick

            if sticks <= 1: #checks if there's less than 2 sticks left (prevents and infinite loop)
                break #breaks the while loop

            if cobble <= 2: #checks if there's less than or equal to two cobble left
                break
            pass
        pass
        if cobble <= 2 or sticks <= 1:
            break
    
    if stone_pick >= 1: #if there's more than or equal to 1 stone pick
        return(stone_pick) #return to the place that called the function the value
    else: 
        print('No picks :(') #print's to terminal if there's no picks
        pass
    

print(arr)

print(stone_pick(arr))
arr = (["Sticks"]*2 + ["Cobblestone"]*1)
print(stone_pick(arr))
arr = (["Sticks"]*4 + ["Wool"]*3 + ["Dirt"]*6)
print(stone_pick(arr))
arr = (["Wood"]*2 + ["Cobblestone"]*12)
print(stone_pick(arr))