import time

# The Rome game
# Supposed to show the rise, expansion and fall of empires
# All through simple terminal prompts...

# Basic Resources
Men = 10
Tablets = 0
Coin = 100
# Buildings
House = 0
Mill = 0
# Advanced Buildings
colouseum = 0

# World Info
season = 'Spring' #Swaps between Spring and Fall to 'emulate' years passing
seaStrength = 100
totalEnemies = 2
enemyMultiplier = 2

# userInfo
expandReady = False


def wait(): # Wait half a year- If buildings are building finish construction...
    print('You wait through the season')
    if season == 'Fall':
        executeActions()

def Expand(Soldiers,season,expandReady): # Send Soldiers off to expand the empire
    expandReady = expandReady
    print(f'You send off {Soldiers} Soldiers in longships and boats')
    if season == 'Spring':
        print(f'They will return in a year')

    if season == 'Fall':
        print('Your soldiers will return in half a year')
    expandReady = True


def build(Men, Tablets, Coin, House, Mill, colouseum): # Construct Buildings
    print('Which building would you like to construct?')
    print('============================================')
    print('| Building | Cost |')
    if Men >= 5:
        print('\'House\': 5 Men')
    if Men >= 10:
        print('\'Stone Quarry\': 10 Men')
    if Men >= 10 & Tablets >= 5:
        print('\'Mill\': 10 Men, 5 Tablets')

def executeActions(): # Execute actions for this season
    if season == 'Spring':
        pass
    if season == 'Fall':
        if expandReady == True:
            print('expand')
            # Resolve expansion
        
        if building == True:
