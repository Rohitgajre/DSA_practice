new_list = []
lst = [2, 7, 21, 34]
T = 9
for i in range(len(lst)):
    for j in range(i+1):
        if lst[i] + lst[j] == T:
            new_list.extend([lst[i], lst[j]])

print(new_list)

# Q.2

# Input: arr[] = [0, 0, 1, 1, 0]
# Output: [0, 0, 0, 1, 1]
# Explanation:  After segregation, all the 0's are on the left and 1's are on the right. Modified array will be [0, 0, 0, 1, 1].
lst = [0, 0, 1, 1, 0]

left = 0
right = len(lst) - 1

while left < right:
    if lst[left] == 0:
        left += 1
    elif lst[right] == 1:
        right -= 1
    else:
        lst[left], lst[right] = lst[right], lst[left]

print(lst)