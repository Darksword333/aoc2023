with open("Day1/input.txt", "r") as f:
    data = f.readlines()

result = 0

for line in data:
    for char in line:
        if char.isdigit():
            first_digit = int(char)
            break

    for char in reversed(line):
        if char.isdigit():
            last_digit = int(char)
            break

    number = int(str(first_digit) + str(last_digit))

    result += number

print(result)
