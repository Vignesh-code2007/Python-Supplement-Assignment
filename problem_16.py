# Problem 16: Find the second largest number in a list
# Find and fix th

numbers = [45, 89, 12, 78, 34]
largest = max(numbers)
numbers.remove(largest)
second_largest = max(numbers)
print(f"Second largest: {second_largest}")

