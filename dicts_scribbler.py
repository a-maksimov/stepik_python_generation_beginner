# put your python code here

d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

string = input()

sum = 0

for char in string:
    for points in d:
        for letter in d[points]:
            if char == letter:
                sum += points
                break

print(sum)