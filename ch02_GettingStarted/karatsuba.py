# Karatsuba Multiplication as example for Divide and Conquer Algorithms
# python 3.6.4

import math

def intDigits(x):
    return len(DigitsArray(x))

def DigitsArray(x):
    return str(int(x))

def splitDigits(x, m):
    if m >= intDigits(x):
        return (0,x)
    digits = DigitsArray(x)
    xHigh, xLow = int(digits[:-m]), int(digits[-m:])
    return (xHigh, xLow)

assert intDigits(5) == 1
assert intDigits(5.0) == 1
assert intDigits(10) == 2
assert intDigits(99) == 2
assert splitDigits(9, 1) == (0,9)
assert splitDigits(99, 1) == (9,9)
assert splitDigits(1234, 2) == (12,34)
assert splitDigits(1234, 3) == (1,234)
assert splitDigits(1234, 4) == (0,1234)
assert splitDigits(12345, 4) == (1,2345)

productCnt = 0

def kmultiply(x,y):
    global productCnt
    #if x==0 or y==0: return 0
    #if x==1: return y
    #if y==1: return x
    if intDigits(x) >= intDigits(y): 
        m = int((intDigits(x)/2)) # py2 rounds to float, py3 to int
    else: 
        m = int((intDigits(y)/2)) # py2 rounds to float, py3 to int
        
    if m <= 0:
        return x*y

    productCnt+=1
    pCnt = productCnt
        
    x1,x0 = splitDigits(x,m)
    y1,y0 = splitDigits(y,m)
    
    z2 = kmultiply(x1,y1) 
    z0 = kmultiply(x0,y0) 
    z1 = kmultiply(x0+x1, y0+y1) - z2 - z0
    
    xy = z2*10**(2*m) + z1*10**m + z0
    
    print('(#{}) K({}): {} X {} =\n[{} {}] X [{} {}] ='.format(
        pCnt, m, x,y, x1,x0, y1,y0))
    print('x1y1.10^{} + x0y1.10^{} + x0y0 ='.format(2*m, m))
    print('({}x{})10^{} + ({}x{} + {}x{})10^{} + {}x{} ='.format(
        x1,y1,2*m, x0,y1,x1,y0,m, x0,y0))
    print('{}*10^{} + {}*10^{} + {} =\n{}'.format(
        z2, 2*m, z1, m, z0,  xy))
    assert xy == x*y, 'Karatsuba error: \nactual  :{} \nexpected:{}'.format(xy,x*y)
    return xy

a, b = 3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627
#a,b = 31415926535897932384626433832795 , 27182818284590452353602874713526
#8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
#a,b = 11111111111111111111111111111111, 11111111111111111111111111111111
#a,b = 1111111111111111, 1111111111111111
#a,b = 111111111111111111111111, 111111111111111111111111
#a, b = 1234, 567
#a, b = 5123435234, 2

c = kmultiply(a,b)
print('karatsuba multiplication: {} X {} = {}'.format(a,b,c))
print('normal multiplication: {} X {} = {}'.format(a,b,a*b))
assert a*b == c, 'karatsuba multiplication error'
print('karatsuba multiplication success')
