def multiply_basic(poly1, poly2):
    P = []
    lenOfP= int(len(poly1) + len(poly2) - 1)
    k = 0 
    while k < lenOfP:

        sumOfProducts = 0
        for i in range(len(poly1)):
            for j in range(len(poly2)):
              
                if i+j == k:
                    
                    sumOfProducts+=poly1[i] * poly2[j]
                    break
                    
        P.append(sumOfProducts)
        k+=1
             
    return P

# print(multiply_basic([x for x in range(2000)], [y for y in range(10)]))
print(multiply_basic([y for y in range(30)], [x for x in range(10)]))

# [1,2] [3,4]