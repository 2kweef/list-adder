numbers = []

while len(numbers) < 10:
    number = int(input("Enter a number: "))
    if number not in numbers:
        numbers.append(number)
print(numbers)
