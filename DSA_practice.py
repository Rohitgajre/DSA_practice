new_list = []
lst = [2, 7, 21, 34]
T = 9
for i in range(len(lst)):
    for j in range(i+1):
        if lst[i] + lst[j] == T:
            new_list.extend([lst[i], lst[j]])

print(new_list)
