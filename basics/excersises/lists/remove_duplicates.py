ll = [1,2,3,4,5,2,3,20,2,1]

# There is a better way to do this but this is just for example
print(ll)
filtered = []
for i in ll:
    if i not in filtered:
        filtered.append(i)
print(filtered)

