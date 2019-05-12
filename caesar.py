from string import ascii_uppercase

with open('2016/dane_6_1.txt') as f:
    data = list(map(str.strip, f.readlines()))
print(data)

def shift(input, k):
    output = ''
    for char in input:
        index = ascii_uppercase.index(char)
        new_index = (index + k) % len(ascii_uppercase)
        output += ascii_uppercase[new_index]
    return output

f = open('wyniki_6_1.txt', 'w')
for i in data:
    f.write('{}\n'.format(shift(i, 107)))
f.close()

# 2
with open('2016/dane_6_2.txt', 'r') as f:
    data2 = list(map(str.split, map(str.strip, f.readlines())))
    for i in range(len(data2)):
        if len(data2[i]) == 2:
            data2[i] = (data2[i][0], int(data2[i][1]))

# for fuck in data2:
#     if len(fuck) != 2:
#         data2.remove(fuck)

# f = open('wyniki_6_2.txt', 'w')
# for i in data2:
#     f.write('{}\n'.format(shift(i[0], -i[1])))
# f.close()

with open('2016/dane_6_3.txt') as f:
    data3 = [tuple(line.split()) for line in f.readlines()]
print(data3)

def can_decrypt(cryptogram, expected):
    for i in range(len(ascii_uppercase)):
        if shift(cryptogram, -i) == expected:
            return True
    return False

encrypted_incorrectly = []
for expected, cryptogram in data3:
    if not can_decrypt(cryptogram, expected):
        encrypted_incorrectly.append(expected)
print(encrypted_incorrectly)