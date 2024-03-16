numbers = [1,2,3,4,5]
n = 2

def remove_all_after(numbers, n):
    new_numbers = []
    for x in numbers:
        new_numbers.append(x)
        if x == n:
           break
    return new_numbers

result = remove_all_after(numbers, n)
print(result)
    
...
