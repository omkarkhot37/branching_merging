x,y,z,a=('omkar','sumit','d','fix 4')

print(x,y,z,a)


#List
x=[23,3,3,2,1,2]
x=x*3
y=x.copy
print(id(y))
print(id(x))

#
#  del x
# How can you get the last three elements of a list?
print(x)
print(x[-3:])
print(x[::-1])
print(x[::])

s='omkar'
print(s[1:5])
print(s[::-1])

#list comprehension

new_list=[a  for a in range(10) if a%2 == 0]
sec_list=[a  for a in range(10) if a%2 == 1]
final=new_list + sec_list
final.sort()
print(final)
final.sort(reverse=True)
print(final)

# Explain the difference between list.append() and list.extend().
new_list.append(sec_list)
print(new_list)
new_list.extend(sec_list)
print(new_list)


# What is the difference between a shallow copy and a deep copy?
# A shallow copy creates a new object but inserts references into it to the objects found in the original

# object. A deep copy creates a new object and recursively adds copies of nested objects found in the original

example_list = [1, 2, [3, 4]]
import copy
shallow_copy = copy.copy(example_list)
deep_copy = copy.deepcopy(example_list)
print(shallow_copy)
print(deep_copy)
print(id(shallow_copy))
print(id(deep_copy))
print(id(example_list))
print(id(example_list[2]))

# Tuples can be unpacked into variables, while lists cannot be unpacked in the same way
x,y,z=(1,2,3)
a,b,c=[1,2,3]
print(x,y,z,a,b,c)


# What is the difference between a tuple and a list?
# A tuple is immutable, meaning it cannot be changed after creation, while a list is mutable and 
# can be modified. Tuples are defined using parentheses, while lists are defined using square brackets
# Tuples can be used as keys in dictionaries, while lists cannot
# Tuples are generally faster than lists for iteration and access due to their immutability

# Tuples can be used to store heterogeneous data, while lists are typically used for homogeneous data
# Tuples can be used to return multiple values from a function, while lists are typically used for single 
# values 
# Tuples can be used to create namedtuples, which are a subclass of tuples that allow for named fields
# Lists can be used to create arrays, which are a more efficient way to store and manipulate large amounts of
# data 
# Tuples can be used to create sets, which are a collection of unique elements
# Lists can be used to create dictionaries, which are a collection of key-value pairs
# Tuples can be used to create frozensets, which are a set that cannot be modified after creation
# Lists can be used to create defaultdicts, which are a dictionary that returns a default value if the key is 
# not found.



dictionary = {'name': 'omkar', 'age': 23, 'city': 'pune','marks':[90,80,70],'subjects':['maths','science','english']}

for a in dictionary.items():
    print(a)


# tuple
# Create a tuple that contains the elements (1, 2, 3) and another tuple (4, 5, 6) as its elements.
a=(1, 2, 3)
b=(4, 5, 6,1,1,14,1)
c=list(a+b)    
print(c)
del c[5]
print(c)
s='omkarkhot'
print(c.count(1))
print(s.count('o'))
id=c.index(1,c.index(1)+1)
print(id-1)
