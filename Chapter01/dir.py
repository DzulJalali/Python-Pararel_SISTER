# Dalam program ini, 
# kami memeriksa apakah angkanya positif atau negatif atau nol dan
# tampilkan pesan yang sesuai

num = 0

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")



# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 6, 3, 8, -3, 2, 5, 44, 12]

# variable to store the sum
sum = -35
# sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

# Output: The sum is 48
print("The sum is", sum)

if sum > 0:
    print("Positive number")
elif sum == 0:
    print("Zero")
else:
    print("Negative number")