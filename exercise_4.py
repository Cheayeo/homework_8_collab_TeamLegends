def chunking_by(numbers, chunks):
    new_list = []
    for x in range(0, len(numbers), chunks):
        new_list.append(numbers[x:(x+chunks)])
    return new_list

print(chunking_by([5, 4, 7, 3, 4, 5, 4], 3))
print(chunking_by([3, 4, 5], 1))
