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
        # print("left", left)
        left += 1
        # print("left .....", lst[left])
    elif lst[right] == 1:
        # print("right", right)
        right -= 1
        # print("right .........")
    else:
        lst[left], lst[right] = lst[right], lst[left]

# print(lst)


# revese the number

# lst = 5483
# num = lst
# count = 0
# while num > 0:
#     count++1
#     num = num/10


'''
* * * *
* * * *
* * * *
* * * *
'''

for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print(" ")

print("------------------------------------------")

'''
00000
0000
000
00
0
'''

for i in range(5):
    for j in range(5-i):
        print("0", end="")
    print("")

print("-----------------------------------------------")

'''
54321
4321
321
21
1
'''

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")

    print("")