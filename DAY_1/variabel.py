a = 5  # integer
A = "hello"  # this is not same as a, variable names are case-sensitive
b = "john"  # string
# b = 'john' this also same as above

x = str(3)   # x will be '3'
y = int(3)   # y will be 3
z = float(3) # z will be 3.0

print(type(x)) # this will show that x is of type 'str'
print(type(y)) # this will show that y is of type 'int'
print(type(z)) # this will show that z is of type 'float'

# you can also assign multiple values to multiple variables in one line
r, s, t = "orange", "banana", "cherry"

# this variable names are valid
myvar = 1
_myvar = 2
my_var = 3

# this variable names are invalid
# 2myvar = 1  # starts with a number
# my-var = 2  # contains a hyphen
# my var = 3  # contains a space

#type variables

myVariableName = "John"  # camel case
my_variable_name = "John"  # snake case
MyVariableName = "John"  # pascal case

d = f = g = "orange"  # all three variables will be assigned the same value

fruits = ["apple", "banana", "cherry"]
q, w, e = fruits  # unpacking a list(array) into variables

word = "Awesome"

def myfunc():
  print("Python is " + word) # this will print "Python is fantastic":

myfunc()