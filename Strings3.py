# string manipulation in Python---------------------


text = 'Hi, hello there'
print(text)  # Output: Hi, hello there

# tripple quotes
text = '''Hi, hello there
multiline string
with an emoji face'''
# print(text)  # Output: Hi, hello there
                # multiline string
                # with an emoji face
 
username = "super_coder"
password = "super_secret"
print(username, password)  # Output: super_coder super_secret

# adding string together
print("Hello " + "World")  # Output: Hello World
print("Hello " + "World" + "!")  # Output: Hello World!

# type conversion
a = str(10)  # Convert integer to string
b = int(a)  # Convert string back to integer
c = float(b)  # Convert integer to float
d = type(c)  # Get the type of c
print(d)

# escape sequences

you_name = "arun pratap singh 'sekhar'"
print(you_name)  # Output: arun pratap singh 'sekhar'

weather = "It's a \"sunny\" day"
print(weather)  # Output: It's a "sunny" day


# formatted strings
name = ("arun")
age = 18
print(f" my name is {name} and i am {age} year old".format(name, age))


name = "Sally"
age = 100
print(f"Hi {name}, you are {age} years old")

# String Indexes

selfish = "01234567"
print(selfish[0])  # Output: 0
print(selfish[7])  # Output: 7
print(selfish)     # Output: 01234567

selfish = "01234567"
print(selfish[0:2])    # Output: 01
print(selfish[0:7])    # Output: 0123456
print(selfish[0:8])    # Output: 01234567

selfish = "01234567"
print(selfish[0:8:2])  # Output: 0246 
# [0:8:2] → 0 se 8 tak, har doosra character lo, toh 0,2,4,6 milega.

selfish = "01234567"
print(selfish[-1])  # Output: 7
print(selfish[-2])  # Output: 6
print(selfish[-3])  # Output: 5


selfish = "01234567"
print(selfish[::-1])  # Output: 76543210


selfish = "01234567"
print(selfish[1:])     # Output: 1234567 (1 se end tak)
print(selfish[:5])     # Output: 01234 (0 se 5 tak, 5 include nahi)
print(selfish[::])     # Output: 01234567 (pura string, step 1)




text = "  Hello World  "
print(text.upper())         # Output: HELLO WORLD
print(text.strip())         # Output: Hello World
print(text.replace("World", "Python"))  # Output:   Hello Python