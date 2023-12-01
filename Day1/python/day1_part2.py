with open("input.txt", "r") as f:
    data = f.readlines()

liste_num = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num_char = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}

result = 0
reconstructed_str = ""
first_digit = 0
last_digit = 0

for line in data:

    for char in line:
        reconstructed_str += char
        if char.isdigit():
            print("ici1", char)
            first_digit = int(char)
            reconstructed_str = ""
            break
        elif not char.isdigit():
            for number in liste_num:
                if number in reconstructed_str:
                    print("la1", number)
                    first_digit = num_char[number]
                    reconstructed_str = ""
                    break
                    
    for char in line:
        reconstructed_str += char
        if char.isdigit():
            print("ici", char)
            last_digit = int(char)
            reconstructed_str = ""
        else:
            for number in liste_num:
                if number in reconstructed_str:
                    print("la", number)
                    last_digit = num_char[number]
                    reconstructed_str = ""

    number = int(str(first_digit) + str(last_digit))
    first_digit = 0
    last_digit = 0

    result += number

print(result)
