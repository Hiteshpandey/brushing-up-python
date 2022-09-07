number = input("Enter a number: ")
number_map = {
    '0' : 'Zero',
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' : 'Four',
    '5' : 'Five',
    '6' : 'Six',
    '7' : 'Seven',
    '8' : 'Eight',
    '9' : 'Nine',
}

# Typecasting the string to list type will create individual characters
nums = list(number.strip())

output = ''
for num in nums:
    # print(number_map[num], end=' ')
    output += number_map.get(num, '[not a number]')+' '
print(output) 
