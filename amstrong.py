# Take input from the user
num = int(input("Enter a number: "))

# Store the original number to compare later
temp = num
digits = len(str(num))
armstrong_sum = 0

# Extract digits and calculate the sum of powers
while temp > 0:
    digit = temp % 10                # Gets the last digit
    armstrong_sum += digit ** digits  # Raises digit to power and adds to sum
    temp //= 10                      # Removes the last digit

# Check if the sum matches the original number
if num == armstrong_sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
