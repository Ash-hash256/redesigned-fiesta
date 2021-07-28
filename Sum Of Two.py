#Algorithm that finds if there is a pair of number from a and b that add up to V 

# Brute force solution

def sumOfTwo1(a,b,v):
    for x in range(0,len(a)):
        for y in range(0,len(b)):
            if int(a[x]) + int(b[y]) == v:
                return True

    else:
        return False

first1 = sumOfTwo1([1,2,3],[10,20,30,40],42)
#second1 = sumOfTwo1([1,2,3],[10,20,30,40],42)
third1 = sumOfTwo1([0,0,-5],[-10,40,-3,9],-8)


print("Test Case 1: {}".format(first1))
#print("Test Case 2: {}".format(second1))
print("Test Case 3: {}".format(third1))

   
# Better solution time complexity   

def sumOfTwo2(a,b,v):
    complements = []

    for x in range(0,len(a)):
        complements.append(v - int(a[x]))

    for z in range(0, len(b)):
        if b[z] in complements:
            return True
    else:
        return False



first2 = sumOfTwo2([1,2,3],[10,20,30,40],42)
#second2 = sumOfTwo2([1,2,3],[10,20,30,40],42)
third2 = sumOfTwo2([0,0,-5],[-10,40,-5,9],-8)


print("Test Case 1: {}".format(first2))
#print("Test Case 2: {}".format(second2))
print("Test Case 3: {}".format(third2))
