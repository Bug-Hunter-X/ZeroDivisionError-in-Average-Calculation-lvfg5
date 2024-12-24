def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]

#The bug is that it will throw an exception if the list is empty
average = calculate_average(my_numbers)
print(f"The average is: {average}")

empty_list = []
average = calculate_average(empty_list)
print(f"The average is: {average}")