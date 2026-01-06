words = []

for i in range(5):
    words.append(input())

results = ''

max_length = max(len(word) for word in words)

for col in range(max_length):
    for row in range(5):
        if col < len(words[row]):
            results += words[row][col]

print(results)