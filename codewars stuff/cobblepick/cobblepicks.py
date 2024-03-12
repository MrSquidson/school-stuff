
arr = (["Sticks"]*4 + ["Cobblestone"]*3)

def stone_pick(arr):
    cobble = 0
    sticks = 0
    stone_pick = 0
    
    for items in arr:
        match items:
            case 'Cobblestone':
                cobble += 1
                pass

            case 'Sticks':
                sticks += 1
                pass

            case 'Wood': # Wood is worth 4 sticks
                sticks += 4
                pass

            case _:
                # Yeah these dont matter
                pass

    while cobble >= 3:
        if sticks >= 2:
            sticks -= 2
            cobble -= 3
            stone_pick += 1

            if sticks <= 1:
                break
            # print('pick++')
            if cobble <= 2:
                break
            pass
        pass
        if cobble <= 2 or sticks <= 1:
            break
    
    if stone_pick >= 1:
        return(stone_pick)
    else: 
        print('No picks :(')
        pass
    

print(arr)

print(stone_pick(arr))
arr = (["Sticks"]*2 + ["Cobblestone"]*1)
print(stone_pick(arr))
arr = (["Sticks"]*4 + ["Wool"]*3 + ["Dirt"]*6)
print(stone_pick(arr))
arr = (["Wood"]*2 + ["Cobblestone"]*12)
print(stone_pick(arr))