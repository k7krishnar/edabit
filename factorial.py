def factorial(num):
    if num >= 1:
        sum = 1
        for item in range(1,num,1):
            sum=sum+(item*sum)
        return sum

# test cases
print(factorial(5))
print(factorial(1))
print(factorial(2))
print(factorial(0))