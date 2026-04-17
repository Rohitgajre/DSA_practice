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

print("----------------------------------")
'''
  0
 000
00000

'''

for i in range(5, 0, -2):
    for j in range(i//2):
        print(" ", end="")
    for K in range(6-i):
            print("0", end="")
    print("")

'''
     0
   0 0 0
 0 0 0 0 0
'''

print("--------------------------------------------------------")

'''
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *


'''
n = 7
for i in range(n):
    for j in range(n):
        print("* ", end=" ")
    print("")

print("-------------------------------------------------------")

'''
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10
'''

for i in range(1, 11):
    for j in range(11):
        print(i, end=" ")
    print("")


print("-----------------------------------------------------")

'''
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10

'''
for i in range(1, 11):
    for j in range(1, 11):
        print(j, end=" ")
    print("")


print("-----------------------------------------------------------")

'''
A A A A A A A A A A
B B B B B B B B B B
C C C C C C C C C C
D D D D D D D D D D
E E E E E E E E E E
F F F F F F F F F F
G G G G G G G G G G
H H H H H H H H H H
I I I I I I I I I I
J J J J J J J J J J
'''
for i in range(10):
    x = chr(65+i)
    for j in range(10):
        print(x, end=" ")
    print("")


print("--------------------------------------------------")

'''
10 10 10 10 10 10 10 10 10 10
9 9 9 9 9 9 9 9 9 9
8 8 8 8 8 8 8 8 8 8
7 7 7 7 7 7 7 7 7 7
6 6 6 6 6 6 6 6 6 6
5 5 5 5 5 5 5 5 5 5
4 4 4 4 4 4 4 4 4 4
3 3 3 3 3 3 3 3 3 3
2 2 2 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 1 1

'''

for i in range(1, 11):
    for j in range(1, 11):
        print(11-i, end=" ")
    print()

print("--------------------------------------------------------------")
'''
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2 1

'''
for i in range(1, 11):
    for j in range(1, 11):
        print(11-j, end=" ")
    print()

print("---------------------------------------------")

'''
J J J J J J J J J J
I I I I I I I I I I
H H H H H H H H H H
G G G G G G G G G G
F F F F F F F F F F
E E E E E E E E E E
D D D D D D D D D D
C C C C C C C C C C
B B B B B B B B B B
A A A A A A A A A A

'''
for i in range(1, 11):
    for j in range(1, 11):
        # print(chr(74-(1-i)), end=" ")
        print(chr(74 - (i - 1)), end=" ")

    print()

print("------------------------------------------------------------")

'''
Pattern-8:
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
J I H G F E D C B A
'''

for i in range(1, 11):
    for j in range(1, 11):
        # print(chr(75-(j-1)), end=" ")
        print(chr(65+10-j), end=" ")
    print()

print("------------------------------------------------------------")

'''
Pattern-9:
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
* * * * * * * * * *
'''

n = 10
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()


print("-----------------------------------------------")

'''
Pattern-10:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
7 7 7 7 7 7 7
8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10

'''
n = 11
for i in range(1, n+1):
    for j in range(1, i):
        print(i-1, end=" ")
    print()


print("----------------------------------------------")

'''
Pattern-11:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9 10

'''
n = 10
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


print("---------------------------------------------------------")
'''
Pattern-12:
A
B B
C C C
D D D D
E E E E E
F F F F F F
G G G G G G G
H H H H H H H H
I I I I I I I I I
J J J J J J J J J J
'''
n = 10
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(64+i), end=" ")
    print()

print("----------------------------------------------")
'''
Pattern-13:
A
A B
A B C
A B C D
A B C D E
A B C D E F
A B C D E F G
A B C D E F G H
A B C D E F G H I
A B C D E F G H I J
'''

n = 10
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(65+j-1), end=" ")
    print()


print("-----------------------------------------------")

'''
Pattern-14:
* * * * * * * * * *
* * * * * * * * *
* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''

for i in range(1, n+1):
    for j in range(1, n+2-i):
        print("* ", end=" ")
    print()


print("---------------------------------------------")

'''
Pattern-15:
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3
4 4 4 4 4 4 4
5 5 5 5 5 5
6 6 6 6 6
7 7 7 7
8 8 8
9 9
10

'''
for i in range(1, n+1):
    for j in range(1, n+2-i):
        print(i, end=" ")
    print()


print("--------------------------------------------")

'''
Pattern-16:
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

'''
n = 10
for i in range(1, n+1):
    for j in range(1, n+2-i):
        print(j, end=" ")
    print()


print("----------------------------------------------------")

'''
Pattern-17:
A A A A A A A A A A
B B B B B B B B B
C C C C C C C C
D D D D D D D
E E E E E E
F F F F F
G G G G
H H H
I I
J
'''

n = 10
for i in range(1, n+1):
    for j in range(1, n+2-i):
        print(chr(64+i), end=" ")
    print()


print("-----------------------------------------------")

'''
Pattern-18:
A B C D E F G H I J
A B C D E F G H I
A B C D E F G H
A B C D E F G
A B C D E F
A B C D E
A B C D
A B C
A B
A

'''
n = 10
for i in range(1, n+1):
    for j in range(1, n+2-i):
        print(chr(64+j), end=" ")
    print()

print("-------------------------------------------------")


'''
Pattern-19:
10 10 10 10 10 10 10 10 10 10
9 9 9 9 9 9 9 9 9
8 8 8 8 8 8 8 8
7 7 7 7 7 7 7
6 6 6 6 6 6
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''

n = 10
for i in range(1, n+1):
    for j in range(1, n+2-i):
        print(n+1-i, end=" ")
    print()


print("-------------------------------------------------s")

'''
Pattern-20:
10 9 8 7 6 5 4 3 2 1
10 9 8 7 6 5 4 3 2
10 9 8 7 6 5 4 3
10 9 8 7 6 5 4
10 9 8 7 6 5
10 9 8 7 6
10 9 8 7
10 9 8
10 9
10

'''

for i in range(1, n+1):
    for j in range(1, n+2-i):
        print(n+1-j, end=" ")
    print()

print("-----------------------------------------------------------")

'''
Pattern-21:
J J J J J J J J J J
I I I I I I I I I
H H H H H H H H
G G G G G G G
F F F F F F
E E E E E
D D D D
C C C
B B
A

'''
for i in range(1, n+1):
    for j in range(1, n+2-i):
        print(chr(65+n-i), end=" ")
    print()


print('-------------------------------------------------------------')

'''
Pattern-22:
J I H G F E D C B A
J I H G F E D C B
J I H G F E D C
J I H G F E D
J I H G F E
J I H G F
J I H G
J I H
J I
J

'''

for i in range(1, n+1):
    for j in range(1, n+2-i):
        print(chr(65+n-j), end=" ")
    print()


'''
Pattern-23:

 *
 **
 ***
 ****
 *****
 ******
 *******
 ********
 ***sss*****
**********
 
'''