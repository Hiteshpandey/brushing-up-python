# Required for deepcopy and copy methods
import copy

# Copy operations can be understood in three steps
# Assgnment, Shallowcopy, Deepcopy

# Step 1
# =============================
# Variable assignment (a = b)
# =============================
# In this case there are two different variables but the same memory assigment
# The list object [1, 2, 3, 4] is stored into the memory
# And the Variable data1 points to that memory location, but in this case there is no duplicate list object created in the memory for data2 variable
# data2 varaible is pointing to the same memory location as data1, since we have used an assigment
# So data1 and data2 are "Referencing" the same memory location

data1 = [1, 2, 3, 4]
data2 = data1
print('data1 :', data1)
print('data2 :', data2)
# This means if we cahange the value of index 0 in data1, it will update the list stored in the memory
# But since data1 and data2 are pointing to the same memory address, it would be reflected on both of the variables when we print them

# We can check the memory location of these variables using id
print('memory data1 : ', id(data1))
print('memory data2 : ', id(data2))

print('Updated data1 list index 0 to 10')
data1[0] = 10
print('data1 :', data1)
print('data2 :', data2)

# Step 2
# =============================================
# Shallow copy can be used to remedy this issue
# =============================================

print('Taking shallow copy')
data2 = data1.copy()
data1[1] = 20

print('data1 :', data1)
print('data2 :', data2)

print('memory data1 : ', id(data1))
print('memory data2 : ', id(data2))

# But let us see what happens in case of nested lists
nlist1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Nested list: ", nlist1)

print("Taking shallow copy to nlist2")
nlist2 = copy.copy(nlist1)

print("modify nlist1 top most index")

# This works
nlist1[0] = ['a', 'b', 'c']

print('nlist1 :', nlist1)
print('nlist2 :', nlist2)


# Creating a copy again to level them
nlist2 = copy.copy(nlist1)

print("modify nlist1 inner index")

# This doesn't work (turning b to d)
nlist1[0][1] = 'd'

print('nlist1 :', nlist1)
print('nlist2 :', nlist2)

# Shallow copy only copies the top most level of the list
# For the inner elements it will save the references to the objects

# So to copy the inner elements of the list object we can used Deepcopy


# Step 3
# ==========
# Deep Copy
# ==========
# This iteratively copies the nested lists. and creates a complete copy of the list object

nlist3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Nested list: ", nlist3)

# Creating a copy again to level them
nlist4 = copy.deepcopy(nlist3)

print("modify nlist3 inner index")

# This doesn't work (turning b to d)
nlist3[0][1] = 'd'

print('nlist3 :', nlist3)
print('nlist4 :', nlist4)