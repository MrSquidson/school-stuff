test = True

def rental_car_cost(d):
    cost = d * 40
    total = 0
    if (d <= 3) == 0:
        total = cost - 20
        print('ran -20')
    if (d <= 7) == 0:
        total = cost - 50
        print('ran -50')
        pass
    
    return(total)

if test == True:
    days = 1
    if rental_car_cost(days) == 40:
        print(f'Returned Correct Answer ({rental_car_cost(days)})')
    else:
        print(f'Returned {rental_car_cost(days)}')
        
    days = 4
    if rental_car_cost(days) == 140:
        print(f'Returned Correct Answer ({rental_car_cost(days)})')
    else:
        print(f'Returned {rental_car_cost(days)}')

    days = 7
    if rental_car_cost(days) == 230:
        print(f'Returned Correct Answer ({rental_car_cost(days)})')
    else:
        print(f'Returned {rental_car_cost(days)}')

    days = 8
    if rental_car_cost(days) == 270:
        print(f'Returned Correct Answer ({rental_car_cost(days)})')
    else:
        print(f'Returned {rental_car_cost(days)}')
