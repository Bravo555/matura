#!/usr/bin/python3

data = []

with open('dane/sygnaly.txt') as f:
    data = list(map(str.strip, f.readlines()))

result = ''

for i in range(39, len(data), 40):
    result += data[i][9]

print(result)

# 2
words = {}
for i in range(len(data)):
    letters = []
    for char in data[i]:
        if char not in letters: letters.append(char);
    words[i] = len(letters)

index = 0
biggest = words[0]

for key, value in words.items():
    if value > biggest:
        index = key
        biggest = value


print(data[index])

# 3
from string import ascii_uppercase

below_10 = []
for word in data:
    max_distance = 10
    below_max = True
    for i in range(len(word) - 1):
        a_index = ascii_uppercase.index(word[i])
        b_index = ascii_uppercase.index(word[i+1])
        distance = abs(a_index - b_index)
        if distance >= max_distance:
            below_max = False
            break
    if below_max == True:
        below_10.append(word)
print(below_10, len(below_10))