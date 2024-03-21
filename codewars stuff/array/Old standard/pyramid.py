# https://www.codewars.com/kata/515f51d438015969f7000013/train/python
def pyramid(n):
    pyramid = []
    passes = 1
    while n > 0:
        layer = '1' * passes
        pyramid.append(layer)
        passes += 1
        n -= 1
        print('did a pass')
        
        test = pyramid * 2
        print(test)
    return pyramid

n = int(input('How many pyramid layers?'))
print(pyramid(n))
