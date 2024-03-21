# URL: https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
#Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
# Examples:

# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    test = False # test field that will display info for every part of the for loop
    realString = "" # Finalized string
    nextCapitalized = False # Value we flip between true and false if we find '_' or '-'
    
    for char in text:
        skipAdding = False # Turns off character skipping
        
        if char == '-': # Found dash
            nextCapitalized = True
            skipAdding = True
            if test == True: print('found - or _') # test line

        if char == '_': # Found Underscore
            nextCapitalized = True
            skipAdding = True
            if test == True: print('found - or _') # test line
        
        if skipAdding == False: # Checks if we skip a character (for example cases where we found - or _)
            if nextCapitalized == False: # Isn't capitalized enabled
                realString = realString + char
                if test == True: print('lowercase') # test line

            if nextCapitalized == True: # Is capitalized enabled
                realString = realString + char.upper()
                nextCapitalized = False
                if test == True: print('Upper') # test line
        if test == True: print(realString) # test line
    return realString



        
    

text = "the-stealth-warrior"
if to_camel_case(text) == "theStealthWarrior":
    print("Works!")
else: 
    print(f'Failed with {to_camel_case(text)}')
text = "The_Stealth_Warrior"
if to_camel_case(text) == "TheStealthWarrior":
    print('Works!')
else: 
    print(f'Failed with {to_camel_case(text)}')
text = "The_Stealth-Warrior"
if to_camel_case(text) == "TheStealthWarrior":
    print('Works!')
else: 
    print(f'Failed with {to_camel_case(text)}')