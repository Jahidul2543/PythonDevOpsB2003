x = 4
print(type(x))
print('My First Script')
name = 'John'
last_name = "Jack"
age = 30
print(name + ' ' + last_name + 'age: ' + str(age))
print(name[1:3])

print("{} Age: {}".format(name, age))

paragraph = """
    Also note that, aside from the zero argument form, 
    super() is not limited to use inside methods. The two 
    argument form specifies the arguments exactly and makes
    the appropriate references. The zero argument form only works
    inside a class definition, as the compiler fills in the 
    necessary details to correctly retrieve the class being defined, 
    as well as accessing the current instance for ordinary methods.

"""

# Use hash sign to comment

price = 10.9900000999999
print(type(price))

# list = []
my_list = [12, 23, 45, 67, 'John']
print("Items in my_list: {}".format(my_list))
length_of_list = len(my_list)
print(length_of_list)
print('Index 1: {}'.format(my_list[1:4]))

"""

Tuple 

"""
# int[] array = new int[6]
# length is fixed
#
my_tuple = (12, 34, 56, 34)
my_list.insert(1, 23000000)
print(my_list)

my_dictionary = {
                 'name': 'John',
                 'City': 'New York',
                 'Zip Code': '12453',
                 'Country': 'USA'
                 }

print('Name: {}'.format(my_dictionary.get('name')))




