def lcm(a, b):

    multiples = []

    for num in range(b, a*b + 1):
        if num % a == 0 and num % b == 0:
            multiples.append(num)

    return min(multiples)

print(lcm(4, 6)) 
print(lcm(9, 6)) 
print(lcm(10, 100))  
print(lcm(13, 17)) 
print(lcm(45, 70)) 
