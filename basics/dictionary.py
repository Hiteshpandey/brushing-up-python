"""
Dictionaries are on of the most useful data structures in python
It is also called as a hash map in other languages
It basically allows us to set a custon index name to a value
In dictionary the values are stored linearly like lists and tuples but in an unorderly fashion
Dictionary allows us to access any value stored any where in the dictionary in a constant timespace no matter how large the stoed data is.
To create a dictionary we need two things {key: value}
We can access any elements in the dictionary immediately by using dictionary[key]
We can store different types of data or nested data in a dictionary with any type of value
"""

# Create a dictionary
customer = {
    "name": "Hitesh",
    "age": 30,
    'verified': True
}

print(customer['name'])

# this will throw an error
# print(customer['xyz'])
# this will also throw an error since keys are case sensitive and Name doesn't exist
# print(customer['Name'])

# To ignore these errors we can use get method of dictionary
print(customer.get('N'))
# providing defalut value
print(customer.get('N', 'Key doesnot exist'))

# Update dictionary
print("Updating customer name")
customer['name'] = 'Hitesh Pandey'
print(customer['name'])

# Add a new key
print('create a new key location')
customer['location'] = 'Mumbai'
print(customer)

# Looping over a dictionary
# with key value
for key, value in customer.items():
    print(f"key {key}, value {value}")