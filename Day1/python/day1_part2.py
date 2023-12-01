with open("Day1/input.txt", "r") as f:
    data = f.readlines()

num_char = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}

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
