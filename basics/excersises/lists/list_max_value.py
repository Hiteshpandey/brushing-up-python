import time

numbers = [4,2,1,9,5,0,8]

# starting timer to check execution time
start_time = time.time()
# Shorthand method
print("max value using inbuilt function: ", max(numbers))
# Calculate difference between start and current time
print("--- %s seconds ---" % (time.time() - start_time))


# Linear search
# Now we assume that minimum of the number would be 0 
# If that minimum value is not set we can use (-sys.maxint) as the default min value

# starting timer to check execution time
start_time = time.time()
max = -1
for i in numbers:
    if (i > max):
        max = i
print("Max value linear search ", max)
print("--- %s seconds ---" % (time.time() - start_time))