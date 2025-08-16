# booleans
# ture and false values for testing purposes



# list 

# question 2 

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[4])
print(numbers[2])

# question 3

fruits = ["apple", "banana", "orange", "mango", "grape"]
print(fruits[0:2])
print(fruits[0::2])
print(fruits[::-1])


# List Slicing

# List slicing strings ki tarah hi kaam karta hai – tu list ke specific parts ko nikal sakta hai using syntax: list[start:stop:step]. Yeh ek naya list return karta hai, original list change nahi hota.

# Start: Kahan se shuru karna hai (default: 0).
# Stop: Kahan tak jana hai (stop index include nahi hota).
# Step: Kitne items skip karne hain (default: 1).

amazon_cart = ["notebooks", "sunglasses", "toys", "grapes"]
print(amazon_cart[0:2])  # Output: ["notebooks", "sunglasses"]
print(amazon_cart[::2])  # Output: ["notebooks", "toys"] (har doosra item)


# Lists are Mutable (Change Kar Sakte Ho)

amazon_cart = ["notebooks", "sunglasses", "toys", "grapes"]
amazon_cart[0] = "laptop"  # Index 0 ko change kiya
print(amazon_cart)  # Output: ["laptop", "sunglasses", "toys", "grapes"]




