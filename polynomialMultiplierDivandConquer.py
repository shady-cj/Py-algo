# To solve the problem using divide and conquer we would have to divide each polynomials into 2 parts 
# e.g A = 3x^3 + 4x^2 + 6x + 4  and B = 4x^2 + 6x + 2 
# we divide each polynomials into 2 different parts 
# A0 = 6x+4  A1 = 4+3x
# B0 = 6x+2 B1 = 4
# Thus having A = A0 + A1(x^2)  Notice the x^2 similarly B = B0 + B1 
# Then to get A*B we do  A0B0 + ((A0+A1)*(B0+B1) - A0B0 - A1B1)x^(n) + (A1B1)x^(2n)
# where n is the half of the length of the array when the polynomial is converted to an array


def multiply_optimized(poly1, poly2, first=True):
    numOfPoly1 = len(poly1)
    numOfPoly2 = len(poly2)
    result = []
    if numOfPoly1 > 1 or numOfPoly2 > 1:
        # n to find the maximum of the 2 polynomials to determine the length of the longest list 
        n = max(numOfPoly1, numOfPoly2)

        # getting the half
        k = int(n//2) 
        
        # We split the array into 2 halves
        A,B = split(poly1, poly2) 
        # destructuring A0, A1,B0, B1
        A0,A1 = A
        B0,B1 = B

        # We find the value of A0B0 and A1B1 recursively
        A0B0 = multiply_optimized(A0, B0,False)
        A1B1 =multiply_optimized(A1, B1,False) 
        # we find the product of (A0+A1)*(B0+B1)
        
        productOfSumAB = multiply_optimized(add(A0,A1),add(B0, B1),False)

        # subract from A0B0 and A1B1 to get ((A0+A1)*(B0+B1) - A0B0 - A1B1)
        differenceOfProductAB =subtract(subtract(productOfSumAB, A0B0), A1B1)
        
        result = add(add(A0B0, increase_exponent(differenceOfProductAB, k)),increase_exponent(A1B1, 2*k))


        #  remove all 0s
        if first:
            
            lenDiff = abs(numOfPoly1-numOfPoly2) -1
            if lenDiff > 0:
                result = result[:-lenDiff]
    elif numOfPoly1 == 1 and numOfPoly2 == 1:
        
        result.append(poly1[0] * poly2[0])
    else:
        result = [] 
    return result



def add(poly1, poly2):
    """Add two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result

def subtract(poly1, poly2):
    """Subract two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] -= poly2[i]
    return result

def split(poly1, poly2):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    # print((poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:]))
    return  (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])


def increase_exponent(poly, n):
    """Multiply poly1 by x^n"""
    return [0] * n + poly

# print(multiply_optimized([x for x in range(2000)], [y for y in range(10)]))
print(multiply_optimized([y for y in range(30)], [x for x in range(10)]))




# 
# def multiply_optimized(poly1, poly2,first=True):
#     numOfPoly1 = len(poly1)
#     numOfPoly2 = len(poly2)
#     result = []
#     if numOfPoly1 > 1 or numOfPoly2 > 1:
#         # n to find the maximum of the 2 polynomials to determine the length of the longest list 
#         n = max(numOfPoly1, numOfPoly2)
       
#         n_diff = abs(numOfPoly1-numOfPoly2)
    
       

     
#         print(poly1,poly2)
#         print(n_diff)

#         # getting the half
#         k = int(n//2) 
        
#         # We split the array into 2 halves
#         A,B = split(poly1, poly2) 
#         # destructuring A0, A1,B0, B1
#         A0,A1 = A
#         B0,B1 = B


#         # We find the value of A0B0 and A1B1 recursively
#         A0B0 = multiply_optimized(A0, B0,False)
#         A1B1 =multiply_optimized(A1, B1,False) 
#         # we find the product of (A0+A1)*(B0+B1)
       
#         print(A1B1)
#         print('------------------------------------------------------------------------------------')
#         productOfSumAB = multiply_optimized(add(A0,A1),add(B0, B1),False)
        

#         # subract from A0B0 and A1B1 to get ((A0+A1)*(B0+B1) - A0B0 - A1B1)
#         differenceOfProductAB =subtract(subtract(productOfSumAB, A0B0), A1B1)
#         # print(A0,A1,B0,B1)
#         # print(productOfSumAB)
#         # print(subtract(productOfSumAB, A0B0))
#         # print(A0B0,A1B1)
#         # print(differenceOfProductAB)
#         # print()
    
#         result = add(add(A0B0, increase_exponent(differenceOfProductAB, k)),increase_exponent(A1B1, 2*k-n_diff))

#     elif numOfPoly1 == 1 and numOfPoly2 == 1:
        
#         result.append(poly1[0] * poly2[0])
#     else:
#         result = [] 
#     return result


