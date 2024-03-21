a = [1,2,2]
b = [1] 
realResult = [2,2]

def array_diff(a, b):
    result = []
    for items in a: # For items i listen 'a'
        print(f'{b} is not supposed to be in result')
        if items == b: # Hvis items er lig med B
            pass
        if b == a: # Hvis items IKKE er i listen 'b'
            pass
        else:
            print(f'appending {items}')
            result.append(items) # Tilføj items der møder kriterierne til listen 'result'
            print(f'Result is now {result}')
      #  if b == result: # Hvis listen 'result' er lig med vores udsmidnings liste ('b') clear 'result' 
       #     print('yea somethings fucked')
        #    result.clear()
         #   print(result)
          #  break
    
            
    return result

if array_diff(a, b) == realResult:
    print('Holy shit i did it')
else:
    print('Not correct')