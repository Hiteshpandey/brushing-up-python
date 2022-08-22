"""
we are gonig to print

*****
**
*****
**
**
"""
# Outer loop will loop 5 times, creating 5 rows
"""
row 1
row 2
row 3
row 4
row 5
"""
# inner loop will loop depending on 0th and 2th position
# we can acheive this by doing mod operation on each index
# if i%2 == 0 which means number is even we print inner loop 5 times, EXCEPT if it is 4 since we want two values there
# else print two times

# inner loop count initialize
inner_loop_count = 0
for i in range(5):
    if (i%2==0 and i != 4):
        # print * 5 times
        inner_loop_count = 5
    else:
        # print * 2 times
        inner_loop_count = 2
    for j in range(inner_loop_count):
        # Print without auto new line
        print('*', end=" ")
    print('\n')

print("Printing using second method")
# Second method by making a list of stars to print
ll = [5, 2, 5, 2, 2]
for i in ll:
    print('*' * i)