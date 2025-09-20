# -------------------------------

num_input = input("Enter a list of numbers separated by commas: ")
numbers = [float(n.strip()) for n in num_input.split(",")]

# Calculate sum, max, and average
total_sum = sum(numbers)
maximum = max(numbers)
average = total_sum / len(numbers)

# Display results
print("\n--- List Calculations ---")
print(f"Sum of elements: {total_sum}")
print(f"Maximum value: {maximum}")
print(f"Average of elements: {average:.2f}")



# Ask the user to input a string
user_string = input("\nEnter a string: ")

# Extract required parts of the string
first_5 = user_string[:5]
last_3 = user_string[-3:]
reversed_string = user_string[::-1]

# Display results
print("\n--- String Operations ---")
print(f"First 5 characters: {first_5}")
print(f"Last 3 characters: {last_3}")
print(f"Reversed string: {reversed_string}")
