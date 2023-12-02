with open("Day1/input.txt", "r") as f:
    data = f.readlines()

result = 0
for line in data:
    line=line.replace("one", "o1ne")
    line=line.replace("two", "t2wo")
    line=line.replace("three", "t3hree")
    line=line.replace("four", "f4our")
    line=line.replace("five", "f5ive")
    line=line.replace("six", "s6ix")
    line=line.replace("seven", "s7even")
    line=line.replace("eight", "e8ight")
    line=line.replace("nine", "n9ine")
    line=line.replace("zero", "z0ero")

    for char in line:
        if char.isdigit():
            first_digit = int(char)
            break
                    
    for char in reversed(line):
        if char.isdigit():
            last_digit = int(char)
            break

    num = int(str(first_digit) + str(last_digit))
    first_digit = 0
    last_digit = 0
    result += num
    num = 0

print(result)