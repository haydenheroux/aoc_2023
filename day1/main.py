with open("data") as file:
    sum = 0

    for line in file:
        nums = []

        for char in line:
            if char.isdigit():
                nums.append(int(char))

        sum += nums[0] * 10 + nums[-1]

    print(sum)

table = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open("data") as file:
    sum = 0

    for line in file:
        buffer = ""
        nums = []

        for char in line:
            buffer += char

            if char.isdigit():
                nums.append(int(char))
                buffer = ""
            else:
                for word in table.keys():
                    if word in buffer:
                        nums.append(table[word])
                        buffer = buffer[-len(word):]

        sum += nums[0] * 10 + nums[-1]

    print(sum)
